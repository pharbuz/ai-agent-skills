#!/usr/bin/env python3
"""AppRole login -> KV v2 read/write, production shape.

Authenticate to Vault with an AppRole role_id/secret_id pair, then write and read
a versioned secret from a KV v2 engine, with explicit error handling.

Env:
    VAULT_ADDR       e.g. https://vault.example.com:8200
    VAULT_ROLE_ID    AppRole role id
    VAULT_SECRET_ID  AppRole secret id
    VAULT_KV_MOUNT   KV v2 mount point (default: "secret")

Run:
    pip install hvac
    python approle_kv.py
"""
from __future__ import annotations

import os
import sys

import hvac
from hvac.exceptions import Forbidden, InvalidPath, VaultError


def build_client() -> hvac.Client:
    """Create a client and authenticate via AppRole. login() sets client.token."""
    client = hvac.Client(url=os.environ["VAULT_ADDR"])
    client.auth.approle.login(
        role_id=os.environ["VAULT_ROLE_ID"],
        secret_id=os.environ["VAULT_SECRET_ID"],
    )
    if not client.is_authenticated():
        raise RuntimeError("Vault authentication failed (check role_id/secret_id)")
    return client


def main() -> int:
    mount = os.environ.get("VAULT_KV_MOUNT", "secret")
    path = "myapp/db"

    try:
        client = build_client()
        kv = client.secrets.kv.v2

        # Write a new version. cas=0 would force create-only; omit to upsert.
        kv.create_or_update_secret(
            path=path,
            mount_point=mount,
            secret={"user": "app", "password": "s3cr3t"},
        )

        # Merge a single key without replacing the whole secret.
        kv.patch(path=path, mount_point=mount, secret={"password": "rotated"})

        # Read the latest version. raise_on_deleted_version pins behavior + silences the warning.
        resp = kv.read_secret_version(
            path=path, mount_point=mount, raise_on_deleted_version=True
        )
        data = resp["data"]["data"]  # NOTE: KV v2 nests payload under data.data
        version = resp["data"]["metadata"]["version"]
        print(f"read {mount}/{path} v{version}: user={data['user']}")

    except InvalidPath:
        print(f"path not found or engine not mounted at '{mount}'", file=sys.stderr)
        return 1
    except Forbidden:
        print("permission denied — token policy lacks capability on this path", file=sys.stderr)
        return 1
    except VaultError as exc:
        print(f"vault error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
