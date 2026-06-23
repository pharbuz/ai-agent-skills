---
name: hvac
description: >-
  Use the `hvac` Python client (import `hvac`) to talk to HashiCorp Vault from
  Python — this is HashiCorp Vault secrets management, NOT HVAC
  heating/ventilation/air-conditioning engineering. Trigger WHENEVER the user
  writes or debugs Python that uses `hvac.Client`, `client.secrets.*`,
  `client.auth.*`, or `client.sys.*`; reads or writes secrets in a Vault KV v1/v2
  engine; uses dynamic secrets (Database, AWS, Azure, GCP), Transit
  encryption-as-a-service, or the PKI certificate engine; authenticates to Vault
  (AppRole, Token, Kubernetes, JWT/OIDC, LDAP, Userpass, AWS, Azure, GCP, TLS
  cert, GitHub, Okta); initializes/seals/unseals a cluster, or manages policies,
  auth methods, secret mounts, leases, audit devices, or Enterprise namespaces;
  or configures TLS verification, retries, a custom requests `Session`, or Vault
  Agent unix-socket access. Covers client setup, authentication, secrets
  engines, the system backend, error handling, and app integration.
---

# hvac — HashiCorp Vault client for Python

`hvac` is the de-facto Python client for [HashiCorp Vault]. It is **synchronous**,
built on `requests`, and maps almost 1:1 onto Vault's HTTP API. Install and
import as `hvac`.

> ⚠️ Disambiguation: this skill is for **HashiCorp Vault** (secrets management).
> It is *not* the HVAC mechanical-engineering library (`TomLXXVI/python-hvac`).
> Despite the `python-hvac.org` docs domain, the package is `hvac` and the import
> is `import hvac`.

```bash
pip install hvac
pip install "hvac[parser]"   # adds optional HCL policy parsing
```

[HashiCorp Vault]: https://developer.hashicorp.com/vault

## Mental model

1. **Create a client** — `hvac.Client(url=..., token=...)`. With no args it
   falls back to the `VAULT_ADDR` / `VAULT_TOKEN` environment variables.
2. **Authenticate**, three ways: pass `token=`, assign `client.token = ...`, or
   call an **auth method** `client.auth.<method>.login(...)` — which by default
   stores the returned token on the client (`use_token=True`). Verify with
   `client.is_authenticated()`.
3. **Operate through three namespaces:**
   - `client.secrets.<engine>.<method>(...)` — secrets engines (KV, Transit, PKI, Database, …)
   - `client.auth.<method>.<method>(...)` — auth method config **and** login
   - `client.sys.<method>(...)` — system backend (init/seal, mounts, policies, health, leases)
4. **Responses are raw JSON dicts** from Vault's API. You index into them —
   e.g. KV v2 read is `resp['data']['data'][key]` (note the **double** `data`).
5. **Failures raise `hvac.exceptions.VaultError` subclasses** mapped to the HTTP
   status (`InvalidPath` = 404, `Forbidden` = 403, …).

```python
import hvac

client = hvac.Client(url="https://127.0.0.1:8200", token="hvs.EXAMPLE")
assert client.is_authenticated()

# write + read a KV v2 secret (engine mounted at the default path "secret/")
client.secrets.kv.v2.create_or_update_secret(path="myapp/db", secret={"password": "s3cr3t"})
resp = client.secrets.kv.v2.read_secret_version(path="myapp/db", raise_on_deleted_version=True)
print(resp["data"]["data"]["password"])      # -> s3cr3t
```

## Creating the client

```python
# TLS (production) — verify defaults to True; point it at a CA bundle if needed
client = hvac.Client(url="https://vault.example.com:8200", token=os.environ["VAULT_TOKEN"])

# Mutual TLS (client certificate auth)
client = hvac.Client(
    url="https://127.0.0.1:8200",
    cert=("/path/client.pem", "/path/client.key"),  # (cert, key)
    verify="/path/server-ca.pem",                   # CA bundle, or True/False
)

# Vault Enterprise namespace
client = hvac.Client(url="https://127.0.0.1:8200", namespace=os.getenv("VAULT_NAMESPACE"))

# Dev only — plaintext HTTP
client = hvac.Client(url="http://127.0.0.1:8200")
```

| Constructor arg | Purpose |
|---|---|
| `url` | Vault address; falls back to `$VAULT_ADDR` |
| `token` | Vault token; falls back to `$VAULT_TOKEN` |
| `verify` | `True` (default) / `False` / path to CA bundle. **hvac verifies TLS by default** |
| `cert` | `(client_cert, client_key)` tuple for mTLS |
| `namespace` | Vault Enterprise namespace |
| `session` | Custom `requests.Session` (retries, proxies, unix socket) → `references/advanced-usage.md` |
| `timeout` | Per-request timeout in seconds (default 30) |
| `adapter` | Custom `hvac.adapters.Adapter` (e.g. `Raw` for raw bytes) |

## Authentication

Calling `client.auth.<method>.login(...)` returns the auth response **and** sets
`client.token` for you (pass `use_token=False` to suppress). Most methods must be
enabled server-side first via `client.sys.enable_auth_method(method_type=...)`.

```python
# AppRole — the standard machine-to-Vault flow
client.auth.approle.login(role_id="<role-id>", secret_id="<secret-id>")

# Userpass / LDAP
client.auth.userpass.login(username="dev", password=os.environ["PW"])
client.auth.ldap.login(username=os.environ["LDAP_USER"], password=os.environ["LDAP_PASS"])

# Kubernetes (in-cluster service-account JWT)
with open("/var/run/secrets/kubernetes.io/serviceaccount/token") as f:
    client.auth.kubernetes.login(role="my-app", jwt=f.read())

# Plain token
client.token = os.environ["VAULT_TOKEN"]
```

| Method | Accessor | | Method | Accessor |
|---|---|---|---|---|
| AppRole | `client.auth.approle` | | LDAP | `client.auth.ldap` |
| Token | `client.auth.token` | | Userpass | `client.auth.userpass` |
| Kubernetes | `client.auth.kubernetes` | | TLS cert | `client.auth.cert` |
| JWT / OIDC | `client.auth.jwt` | | GitHub | `client.auth.github` |
| AWS | `client.auth.aws` | | Okta | `client.auth.okta` |
| Azure | `client.auth.azure` | | GCP | `client.auth.gcp` |

Full login signatures, role/config setup, `use_token`, and custom `mount_point`
→ [`references/authentication.md`](references/authentication.md).

## Secrets engines

`client.secrets.<engine>`. KV v2 is the most common; it versions secrets and
**nests the payload under `data.data`** (metadata under `data.metadata`):

```python
kv = client.secrets.kv.v2
kv.create_or_update_secret(path="myapp/db", secret={"user": "app", "password": "s3cr3t"})
kv.patch(path="myapp/db", secret={"password": "rotated"})        # merge, don't replace
secret = kv.read_secret_version(path="myapp/db", raise_on_deleted_version=True)["data"]["data"]
kv.list_secrets(path="myapp/")                                    # keys under a prefix
kv.delete_latest_version_of_secret(path="myapp/db")              # soft delete (recoverable)
```

KV **v1** is flat (no versioning): `client.secrets.kv.v1.read_secret(path)["data"][key]`.

| Engine | Accessor | Use |
|---|---|---|
| KV v2 / v1 | `client.secrets.kv.v2` / `.v1` | Static secrets (versioned / flat) |
| Transit | `client.secrets.transit` | Encryption-as-a-service (data never stored) |
| Database | `client.secrets.database` | Dynamic, short-lived DB credentials |
| PKI | `client.secrets.pki` | Issue / sign / revoke X.509 certs |
| AWS / Azure / GCP | `client.secrets.aws` / `.azure` / `.gcp` | Dynamic cloud credentials |
| Identity | `client.secrets.identity` | Entities, groups, identity tokens |
| Transform | `client.secrets.transform` | FPE / tokenization / masking (Enterprise) |
| AD / LDAP | `client.secrets.ad` / `.ldap` | Rotated service-account credentials |

Per-engine method signatures, base64 handling for Transit, dynamic-secret
leasing, and PKI issuance → [`references/secrets-engines.md`](references/secrets-engines.md).

## System backend (`client.sys`)

Operational / admin plane: cluster lifecycle, mounts, policies, leases, health.

```python
# Cluster bootstrap (one-time)
if not client.sys.is_initialized():
    result = client.sys.initialize(secret_shares=5, secret_threshold=3)
    client.token = result["root_token"]
client.sys.submit_unseal_keys(result["keys"])   # or submit_unseal_key() one at a time

# Mount a KV v2 engine, write an ACL policy, enable an auth method
client.sys.enable_secrets_engine(backend_type="kv", path="apps", options={"version": "2"})
client.sys.create_or_update_policy(name="app-ro", policy='path "apps/data/myapp/*" { capabilities = ["read"] }')
client.sys.enable_auth_method(method_type="approle")

client.sys.read_health_status(method="GET")      # health / seal status
```

Mounts, tuning, policy/lease/audit/namespace/token management, and response
wrapping → [`references/system-backend.md`](references/system-backend.md).

## Error handling

All errors derive from `hvac.exceptions.VaultError`, sub-typed by HTTP status:

| Exception | Status | Typical cause |
|---|---|---|
| `InvalidRequest` | 400 | Malformed request / missing params |
| `Unauthorized` | 401 | Missing or invalid token |
| `Forbidden` | 403 | Token lacks the policy capability (permission denied) |
| `InvalidPath` | 404 | Path doesn't exist **or** engine not mounted there |
| `RateLimitExceeded` | 429 | Quota / rate limit |
| `InternalServerError` | 500 | Server-side error |
| `VaultDown` | 503 | Vault sealed or in standby |

```python
from hvac.exceptions import Forbidden, InvalidPath, VaultError

try:
    secret = client.secrets.kv.v2.read_secret_version(path="myapp/db", raise_on_deleted_version=True)
except InvalidPath:
    secret = None                  # never written, or wrong mount_point
except Forbidden:
    raise                          # token policy issue — don't silently swallow
except VaultError as e:            # catch-all base
    log.error("vault error: %s", e)
```

## Common pitfalls

- **KV v2 double `data`.** Read returns `resp["data"]["data"][key]`. KV v1 is single
  `resp["data"][key]`. Mixing them up is the #1 KV bug.
- **404 means path *or* mount.** `InvalidPath` fires both when a secret was never
  written and when the engine isn't mounted at that `mount_point` — check both.
- **KV v2 paths carry `data/` / `metadata/` in policies**, not in client calls.
  Client: `path="myapp/db"`. ACL policy: `path "secret/data/myapp/db"`.
- **`read_secret_version` deprecation.** Pass `raise_on_deleted_version=True`
  (or `False`) explicitly to silence the warning and pin behavior.
- **Transit needs base64.** `plaintext`/`hash_input`/`context`/`nonce` must be
  base64-encoded; ciphertext comes back as `vault:v1:...`. See the `base64ify`
  helper in `references/secrets-engines.md`.
- **`login()` mutates the client.** It sets `client.token`. Pass `use_token=False`
  if you only want the response (e.g. minting a token for another principal).
- **TLS verify default differs from the URL.** `verify=True` by default — give it
  a CA bundle path for private CAs rather than disabling verification.
- **Sealed Vault → `VaultDown`/503.** Unseal (`submit_unseal_keys`) before secret ops.

## Reference files

- [`references/authentication.md`](references/authentication.md) — every auth method, login signatures, role/config setup, `use_token`, `mount_point`
- [`references/secrets-engines.md`](references/secrets-engines.md) — KV v1/v2, Transit (+base64), Database/AWS/Azure/GCP dynamic secrets, PKI, Identity, enabling engines
- [`references/system-backend.md`](references/system-backend.md) — init/seal/unseal, mounts & tuning, ACL policies, leases, audit devices, namespaces, token mgmt, wrapping
- [`references/advanced-usage.md`](references/advanced-usage.md) — custom `Session`/retries, private-CA TLS, Vault Agent unix socket, raw adapter calls, namespaces, integration patterns

## Example scripts

- [`examples/approle_kv.py`](examples/approle_kv.py) — AppRole login → KV v2 read/write with error handling (production shape)
- [`examples/transit_encrypt.py`](examples/transit_encrypt.py) — Transit encrypt/decrypt round-trip with base64 handling
- [`examples/bootstrap_init_unseal.py`](examples/bootstrap_init_unseal.py) — initialize, unseal, and mount an engine on a fresh cluster
