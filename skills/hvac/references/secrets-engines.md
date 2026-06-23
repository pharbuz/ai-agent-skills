# hvac — Secrets engines

Secrets engines live under `client.secrets.<engine>`. Enable one server-side with
the system backend before use:

```python
client.sys.enable_secrets_engine(backend_type="kv", path="apps", options={"version": "2"})
client.sys.enable_secrets_engine(backend_type="transit")     # mounts at "transit/"
client.sys.list_mounted_secrets_engines()
client.sys.disable_secrets_engine(path="apps")
```

Every method takes `mount_point=` (default = the engine name, e.g. `secret` for
KV, `transit`, `database`, `pki`).

---

## KV v2 — versioned static secrets (default at `secret/`)

The payload is **nested under `data.data`**; metadata under `data.metadata`.

```python
kv = client.secrets.kv.v2     # or client.secrets.kv (delegates to the default version)

# write / update — cas enforces optimistic concurrency (0 = create-only)
kv.create_or_update_secret(path="myapp/db", secret={"user": "app", "password": "s3cr3t"}, cas=0)

# merge new/changed keys without replacing the whole secret (needs a prior write)
kv.patch(path="myapp/db", secret={"password": "rotated"})

# read latest, or a specific version
resp = kv.read_secret_version(path="myapp/db", raise_on_deleted_version=True)
data = resp["data"]["data"]                     # {"user": ..., "password": ...}
old  = kv.read_secret_version(path="myapp/db", version=1, raise_on_deleted_version=True)

kv.list_secrets(path="myapp/")["data"]["keys"]  # child keys under a prefix

# soft delete (recoverable) vs destroy (permanent)
kv.delete_latest_version_of_secret(path="myapp/db")
kv.delete_secret_versions(path="myapp/db", versions=[1, 2])
kv.undelete_secret_versions(path="myapp/db", versions=[1, 2])
kv.destroy_secret_versions(path="myapp/db", versions=[1])     # irreversible

# metadata / retention
kv.read_secret_metadata(path="myapp/db")
kv.update_metadata(path="myapp/db", max_versions=10, cas_required=True, delete_version_after="720h")
kv.delete_metadata_and_all_versions(path="myapp/db")          # nuke the whole path
```

**`cas` (check-and-set):** `cas=0` writes only if the key doesn't exist;
`cas=N` writes only if the current version is exactly `N`. Returns `400` on
mismatch. Required when the mount has `cas_required=True`.

## KV v1 — flat, unversioned

```python
v1 = client.secrets.kv.v1
v1.create_or_update_secret(path="myapp", secret={"password": "s3cr3t"})
v1.read_secret(path="myapp")["data"]["password"]    # single 'data', no version
v1.list_secrets(path="")
v1.delete_secret(path="myapp")
```

Set the default version once if your `secret/` mount is v1:
`client.secrets.kv.default_kv_version = 1`.

---

## Transit — encryption-as-a-service (Vault never stores your data)

Inputs (`plaintext`, `hash_input`, `context`, `nonce`) must be **base64-encoded**.
Ciphertext returns as `vault:v1:...` (the `v1` is the key version).

```python
import base64

def base64ify(bytes_or_str):
    data = bytes_or_str.encode("utf-8") if isinstance(bytes_or_str, str) else bytes_or_str
    return base64.b64encode(data).decode("ascii")

t = client.secrets.transit
t.create_key(name="app-key", key_type="aes256-gcm96")

ct = t.encrypt_data(name="app-key", plaintext=base64ify("hello"))["data"]["ciphertext"]
pt = t.decrypt_data(name="app-key", ciphertext=ct)["data"]["plaintext"]
plaintext = base64.b64decode(pt).decode("utf-8")            # -> "hello"

# rotate the key, then re-encrypt old ciphertext to the latest version (no plaintext exposure)
t.rotate_key(name="app-key")
ct2 = t.rewrap_data(name="app-key", ciphertext=ct)["data"]["ciphertext"]

# envelope encryption: get a data key (returns both plaintext + wrapped forms)
dk = t.generate_data_key(name="app-key", key_type="plaintext")["data"]

# signing (asymmetric keys: ed25519 / ecdsa / rsa)
t.create_key(name="sign-key", key_type="ed25519")
sig = t.sign_data(name="sign-key", hash_input=base64ify("msg"))["data"]["signature"]
ok  = t.verify_signed_data(name="sign-key", hash_input=base64ify("msg"), signature=sig)["data"]["valid"]
```

---

## Database — dynamic, short-lived DB credentials

```python
db = client.secrets.database
db.configure(name="my-pg", plugin_name="postgresql-database-plugin",
             connection_url="postgresql://{{username}}:{{password}}@db:5432/postgres",
             allowed_roles=["readonly"], username="vault", password="vault-pw")
db.create_role(name="readonly", db_name="my-pg",
               creation_statements=['CREATE ROLE "{{name}}" WITH LOGIN PASSWORD \'{{password}}\' VALID UNTIL \'{{expiration}}\';'],
               default_ttl="1h", max_ttl="24h")

creds = db.generate_credentials(name="readonly")["data"]   # {"username": ..., "password": ...}
# creds are leased — Vault revokes them at TTL. Renew/revoke via client.sys lease APIs.

db.rotate_root_credentials(name="my-pg")                    # rotate the configured root password
db.create_static_role(name="app-static", db_name="my-pg", username="app", rotation_period="24h")
db.get_static_credentials(name="app-static")
```

Cloud equivalents follow the same shape:

- **AWS** `client.secrets.aws` — `configure_root_iam_credentials`, `create_or_update_role`, `generate_credentials`
- **Azure** `client.secrets.azure` — `configure`, `create_or_update_role`, `generate_credentials`
- **GCP** `client.secrets.gcp` — `configure`, `create_or_update_roleset`, `generate_service_account_key` / OAuth token

## PKI — issue and manage X.509 certificates

```python
pki = client.secrets.pki
pki.generate_root(type="internal", common_name="example.com Root CA", mount_point="pki")
pki.create_or_update_role(name="example-dot-com", extra_params={
    "allowed_domains": ["example.com"], "allow_subdomains": True, "max_ttl": "72h"})

issued = pki.generate_certificate(name="example-dot-com", common_name="app.example.com")["data"]
issued["certificate"], issued["private_key"], issued["serial_number"]

pki.sign_certificate(name="example-dot-com", csr=my_csr, common_name="app.example.com")
pki.revoke_certificate(serial_number=issued["serial_number"])
pki.read_crl()
```

## Identity — entities, groups, identity tokens

```python
idn = client.secrets.identity
eid = idn.create_or_update_entity(name="alice", policies=["app-ro"])["data"]["id"]
idn.create_or_update_group(name="admins", policies=["admin"], member_entity_ids=[eid])
idn.create_or_update_entity_alias(name="alice", canonical_id=eid, mount_accessor=auth_accessor)
```

## Other engines

- **Transform** `client.secrets.transform` — format-preserving encryption,
  tokenization, masking (Enterprise). Roles, transformations, templates, alphabets.
- **Active Directory** `client.secrets.ad` / **LDAP** `client.secrets.ldap` —
  `configure`, `create_or_update_static_role`, `generate_static_credentials`,
  `rotate_static_credentials` for rotated service-account passwords.

---

## Notes

- **Leases.** Dynamic secrets (Database/AWS/Azure/GCP/PKI) return a `lease_id`
  and `lease_duration`. Renew/revoke them via the system backend
  (`client.sys.renew_lease` / `revoke_lease`) — see `references/system-backend.md`.
- **`mount_point` everywhere.** If you mounted KV at `apps/`, every call needs
  `mount_point="apps"`; otherwise you get `InvalidPath` (404).
- **KV v2 path vs policy path.** Client calls use the bare logical path
  (`path="myapp/db"`); ACL policies must include the API segment
  (`secret/data/myapp/db` for reads/writes, `secret/metadata/myapp/db` for
  metadata/list).
