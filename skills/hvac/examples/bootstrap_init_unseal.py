#!/usr/bin/env python3
"""Initialize, unseal, and mount an engine on a fresh Vault cluster.

For bootstrapping a brand-new (uninitialized) Vault — typically dev/test or the
very first run of a new cluster. In production, prefer auto-unseal (cloud KMS)
and never print/keep unseal keys or the root token in plaintext.

Env:
    VAULT_ADDR  e.g. https://127.0.0.1:8200

Run:
    pip install hvac
    python bootstrap_init_unseal.py
"""
from __future__ import annotations

import os

import hvac

SHARES = 5
THRESHOLD = 3


def main() -> int:
    client = hvac.Client(url=os.environ.get("VAULT_ADDR", "http://127.0.0.1:8200"))

    # 1. Initialize (one-time). Returns unseal keys + the initial root token.
    if client.sys.is_initialized():
        print("already initialized; provide existing keys/token out of band")
        return 0

    result = client.sys.initialize(secret_shares=SHARES, secret_threshold=THRESHOLD)
    unseal_keys = result["keys"]
    client.token = result["root_token"]
    print(f"initialized: {SHARES} keys, threshold {THRESHOLD}")
    # !! store unseal_keys and result['root_token'] securely — this is the only time you see them

    # 2. Unseal by submitting `threshold` keys.
    if client.sys.is_sealed():
        client.sys.submit_unseal_keys(unseal_keys[:THRESHOLD])
    print(f"sealed: {client.sys.is_sealed()}")

    # 3. Mount a KV v2 engine and write a smoke-test secret.
    client.sys.enable_secrets_engine(
        backend_type="kv", path="apps", options={"version": "2"}
    )
    client.secrets.kv.v2.create_or_update_secret(
        path="bootstrap/check", mount_point="apps", secret={"ok": "true"}
    )
    resp = client.secrets.kv.v2.read_secret_version(
        path="bootstrap/check", mount_point="apps", raise_on_deleted_version=True
    )
    print(f"smoke test: apps/bootstrap/check -> {resp['data']['data']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
