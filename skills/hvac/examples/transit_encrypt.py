#!/usr/bin/env python3
"""Transit encrypt/decrypt round-trip.

The Transit engine is encryption-as-a-service: Vault holds the key and performs
the crypto, but never stores your data. All inputs must be base64-encoded;
ciphertext is returned as "vault:v<n>:...".

Env:
    VAULT_ADDR        e.g. https://vault.example.com:8200
    VAULT_TOKEN       a token with capabilities on the transit mount
    VAULT_TRANSIT_MOUNT  transit mount point (default: "transit")

Run:
    pip install hvac
    # one-time server setup (or do it via client.sys.enable_secrets_engine):
    #   vault secrets enable transit
    python transit_encrypt.py
"""
from __future__ import annotations

import base64
import os

import hvac


def base64ify(bytes_or_str) -> str:
    """Vault Transit requires base64-encoded inputs."""
    data = bytes_or_str.encode("utf-8") if isinstance(bytes_or_str, str) else bytes_or_str
    return base64.b64encode(data).decode("ascii")


def main() -> int:
    mount = os.environ.get("VAULT_TRANSIT_MOUNT", "transit")
    key_name = "example-key"
    message = "hi its me hvac"

    client = hvac.Client(url=os.environ["VAULT_ADDR"], token=os.environ["VAULT_TOKEN"])
    transit = client.secrets.transit

    # Idempotent: create_key is a no-op if the key already exists.
    transit.create_key(name=key_name, mount_point=mount, key_type="aes256-gcm96")

    enc = transit.encrypt_data(
        name=key_name, mount_point=mount, plaintext=base64ify(message)
    )
    ciphertext = enc["data"]["ciphertext"]  # e.g. "vault:v1:abc123..."
    print(f"ciphertext: {ciphertext}")

    dec = transit.decrypt_data(name=key_name, mount_point=mount, ciphertext=ciphertext)
    recovered = base64.b64decode(dec["data"]["plaintext"]).decode("utf-8")
    print(f"decrypted:  {recovered}")

    assert recovered == message, "round-trip mismatch"

    # Rotate the key, then upgrade old ciphertext to the new version without
    # ever exposing plaintext.
    transit.rotate_key(name=key_name, mount_point=mount)
    rewrapped = transit.rewrap_data(name=key_name, mount_point=mount, ciphertext=ciphertext)
    print(f"rewrapped:  {rewrapped['data']['ciphertext']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
