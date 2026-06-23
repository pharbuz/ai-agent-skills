# hvac — Authentication methods

Auth methods live under `client.auth.<method>`. A `login(...)` call returns the
raw auth response **and**, by default, stores the issued token on the client:

```python
resp = client.auth.approle.login(role_id=rid, secret_id=sid)
resp["auth"]["client_token"]   # the token (also now set as client.token)
client.is_authenticated()      # True
```

Cross-cutting kwargs available on most `login()` / config calls:

- **`use_token=True`** (default) — store the returned token on the client.
  Pass `use_token=False` when you only want the response (e.g. minting a token
  for a different principal, or inspecting without re-authenticating).
- **`mount_point="..."`** — the path the auth method is mounted at. Defaults to
  the method name (`approle`, `ldap`, …); set it when mounted elsewhere.

Enable a method server-side before using it:

```python
client.sys.enable_auth_method(method_type="approle", path="approle")
client.sys.list_auth_methods()          # what's enabled
client.sys.disable_auth_method(path="approle")
```

---

## AppRole — machine-to-Vault (most common in production)

```python
# (admin) create the role and fetch its credentials
client.auth.approle.create_or_update_approle(
    role_name="my-app",
    token_policies=["app-ro"],
    token_type="service",
    secret_id_ttl="10m",
    token_ttl="20m",
    token_max_ttl="30m",
    secret_id_num_uses=40,
)
role_id = client.auth.approle.read_role_id(role_name="my-app")["data"]["role_id"]
secret_id = client.auth.approle.generate_secret_id(
    role_name="my-app",
    cidr_list=["127.0.0.1/32"],
)["data"]["secret_id"]

# (app) log in with the pair
client.auth.approle.login(role_id=role_id, secret_id=secret_id)
```

`role_id` is static config; `secret_id` is the rotating secret. Deliver them to
the app separately (e.g. role_id baked in, secret_id response-wrapped — see
`references/system-backend.md` wrapping).

## Token

```python
client.token = os.environ["VAULT_TOKEN"]          # simplest
client.auth.token.create(policies=["app-ro"], ttl="1h")   # mint a child token
client.auth.token.lookup_self()                   # inspect current token
client.auth.token.renew_self(increment="1h")      # extend TTL
client.auth.token.revoke_self()                   # log out
```

## Userpass

```python
client.auth.userpass.create_or_update_user(username="dev", password="pw", policies=["app-ro"])
client.auth.userpass.login(username="dev", password="pw")
```

## LDAP

```python
client.auth.ldap.configure(url="ldap://ldap.example.com", userdn="ou=Users,dc=example,dc=com", ...)
client.auth.ldap.login(username=os.environ["LDAP_USER"], password=os.environ["LDAP_PASS"])
```

## Kubernetes — in-cluster workloads

```python
client.auth.kubernetes.configure(kubernetes_host="https://kubernetes.default.svc")
client.auth.kubernetes.create_role(name="my-app", bound_service_account_names=["my-sa"],
                                    bound_service_account_namespaces=["default"], policies=["app-ro"])
with open("/var/run/secrets/kubernetes.io/serviceaccount/token") as f:
    client.auth.kubernetes.login(role="my-app", jwt=f.read())
```

## JWT / OIDC

```python
# JWT (machine): exchange a signed JWT for a Vault token
client.auth.jwt.jwt_login(role="my-app", jwt=signed_jwt)

# OIDC (human): get the auth URL, complete the browser flow, exchange the callback
auth_url = client.auth.jwt.oidc_authorization_url_request(role="dev", redirect_uri="http://localhost:8250/oidc/callback")
```

## TLS client certificate (`cert`)

```python
client = hvac.Client(url="https://127.0.0.1:8200", cert=("client.pem", "client.key"), verify="ca.pem")
client.auth.cert.login()                          # uses the client cert from the session
```

## Cloud IAM auth

```python
# AWS — IAM or EC2 identity
client.auth.aws.iam_login(access_key, secret_key, session_token, role="my-app")

# Azure — managed identity / service principal
client.auth.azure.login(role="my-app", jwt=azure_jwt, subscription_id=..., resource_group_name=..., vm_name=...)

# GCP — service account JWT
client.auth.gcp.login(role="my-app", jwt=signed_gcp_jwt)
```

## GitHub / Okta

```python
client.auth.github.login(token=os.environ["GITHUB_TOKEN"])
client.auth.okta.login(username="dev", password="pw")
```

---

## Notes

- **Token lifecycle.** Tokens have a TTL and max-TTL. Long-running apps should
  renew (`renew_self`) before expiry or re-`login()`. Vault Agent / the
  [agent unix socket](advanced-usage.md) can manage this outside your process.
- **`create_or_update_approle` vs `create_role`.** Names differ per method
  (AppRole uses `create_or_update_approle`; Kubernetes/JWT use `create_role`).
  When unsure, the method maps to the underlying Vault API path.
- **Response shape.** IDs and tokens live under `resp["data"][...]` for reads
  (`role_id`, `secret_id`) and under `resp["auth"]["client_token"]` for logins.
