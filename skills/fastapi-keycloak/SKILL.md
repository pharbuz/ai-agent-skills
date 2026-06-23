---
name: fastapi-keycloak
description: >-
  Use the `fastapi-keycloak` library (import `fastapi_keycloak`) to integrate
  Keycloak OpenID Connect with FastAPI. Trigger WHENEVER the user adds Keycloak
  auth to FastAPI, protects endpoints with JWT/roles, implements the password or
  authorization_code OAuth2 flow, manages Keycloak users/roles/groups via the
  Admin API, or mentions `FastAPIKeycloak`, `OIDCUser`, `get_current_user`,
  `exchange_authorization_code`, `user_login`, or `add_swagger_config`. Covers
  `FastAPIKeycloak` setup, `get_current_user(required_roles=...)`, login/callback/
  refresh/logout URIs, user/role/group CRUD, identity providers, token validation,
  and Keycloak realm/client configuration for `admin-cli`.
---

# fastapi-keycloak — Keycloak OIDC for FastAPI

[`fastapi-keycloak`] wraps Keycloak's OpenID Connect and Admin REST APIs for
FastAPI. Install and import as `fastapi_keycloak`.

```bash
pip install fastapi_keycloak
```

> This is **fastapi-keycloak/fastapi-keycloak** — not a hand-rolled JWT validator.
> For manual OIDC/JWKS integration without this library, use a different approach.

[`fastapi-keycloak`]: https://github.com/fastapi-keycloak/fastapi-keycloak

## Mental model

1. **Create one `FastAPIKeycloak` instance** (`idp`) with server URL, realm,
   client credentials, `admin-cli` secret, and `callback_uri`. On init it fetches
   an admin token for Admin API calls.
2. **Call `idp.add_swagger_config(app)`** so Swagger UI can authorize with PKCE
   without exposing secrets in the UI.
3. **Protect routes** with `Depends(idp.get_current_user())` or
   `Depends(idp.get_current_user(required_roles=["admin"]))`. Returns `OIDCUser`
   parsed from the Bearer JWT (signed by Keycloak's private key).
4. **Auth flows** — `password` via `idp.user_login()`, `authorization_code` via
   redirect to `idp.login_uri` then `idp.exchange_authorization_code()` on
   callback. Refresh with `idp.refresh_token()`.
5. **Admin operations** — users, roles, groups, identity providers via methods
   on the same `idp` instance (uses `admin-cli` service account).

## Setup

```python
from fastapi import FastAPI, Depends
from fastapi_keycloak import FastAPIKeycloak, OIDCUser

app = FastAPI()
idp = FastAPIKeycloak(
    server_url="http://localhost:8085/auth",   # include /auth on Keycloak ≤21
    client_id="test-client",
    client_secret="your-client-secret",
    admin_client_secret="admin-cli-secret",
    realm="Test",
    callback_uri="http://localhost:8081/callback",
    # optional:
    # admin_client_id="admin-cli",  # default
    # scope="openid profile email",
    # timeout=10,
    # ssl_verification=True,
    # algorithms=["RS256"],
)
idp.add_swagger_config(app)
```

| Parameter | Purpose |
|-----------|---------|
| `server_url` | Keycloak base URL **with `/auth` suffix** (legacy path layout) |
| `client_id` / `client_secret` | App client for user-facing OAuth flows |
| `admin_client_secret` | Secret for `admin-cli` (Admin API) |
| `callback_uri` | Must match a **Valid Redirect URI** in Keycloak |

## Protect endpoints

```python
@app.get("/user")
def current_user(user: OIDCUser = Depends(idp.get_current_user())):
    return user

@app.get("/admin")
def admin_only(user: OIDCUser = Depends(idp.get_current_user(required_roles=["admin"]))):
    return f"Hi admin {user}"

@app.get("/user/roles")
def user_roles(user: OIDCUser = Depends(idp.get_current_user())):
    return user.roles  # merges realm + client roles from JWT
```

- `get_current_user(extra_fields=[...])` copies extra JWT claims into
  `user.extra_fields`.
- Missing/invalid token → `401`. Missing required role → `403`.
- `OIDCUser.roles` raises `KeycloakError` if the token has no roles.

## OAuth2 flows

### Authorization code (browser / SPA backend)

```python
from fastapi.responses import RedirectResponse

@app.get("/login")
def login():
    return RedirectResponse(idp.login_uri)

@app.get("/callback")
def callback(session_state: str, code: str):
    token = idp.exchange_authorization_code(session_state=session_state, code=code)
    return token  # KeycloakToken: access_token, refresh_token, id_token
```

Frontend stores `access_token` and sends `Authorization: Bearer <token>` on API calls.

### Password grant

```python
from fastapi_keycloak import UsernamePassword

@app.post("/token")
def login(credentials: UsernamePassword):
    return idp.user_login(
        username=credentials.username,
        password=credentials.password.get_secret_value(),
    )
```

Raises `HTTPException(401)` on bad credentials. On mandatory actions (verify email,
configure TOTP, update password/profile/locale) raises typed `MandatoryActionException`
subclasses — check `user.requiredActions` via `idp.get_user()`.

### Refresh token

```python
@app.post("/refresh")
def refresh(refresh_token: str):
    return idp.refresh_token(refresh_token)
```

### Useful URIs

| Property | Use |
|----------|-----|
| `idp.login_uri` | Redirect user to Keycloak login |
| `idp.logout_uri` | End session |
| `idp.token_uri` | Token endpoint (used internally) |
| `idp.authorization_uri` | Authorization endpoint |

## Admin API — users

| Method | Description |
|--------|-------------|
| `create_user(first_name, last_name, username, email, password, ...)` | Create user; optional `initial_roles`, `send_email_verification`, `attributes` |
| `get_user(user_id=...)` or `get_user(query="username=foo")` | Lookup by ID or query string |
| `get_all_users()` | List all realm users |
| `update_user(user: KeycloakUser)` | Full user object replace |
| `delete_user(user_id)` | Delete user |
| `change_password(user_id, new_password, temporary=False)` | Reset password |
| `send_email_verification(user_id)` | Trigger verify-email |

## Admin API — roles

| Method | Description |
|--------|-------------|
| `create_role(role_name)` | Create realm role |
| `get_all_roles()` / `get_roles(role_names)` | List / filter roles |
| `get_user_roles(user_id)` | Roles assigned to user |
| `add_user_roles(roles, user_id)` / `remove_user_roles(roles, user_id)` | Assign / revoke |
| `delete_role(role_name)` | Delete realm role |

## Admin API — groups

| Method | Description |
|--------|-------------|
| `create_group(group_name, parent=None)` | Create top-level or nested group |
| `get_all_groups()` / `get_group(group_id)` / `get_group_by_path(path)` | Read groups |
| `get_user_groups(user_id)` / `get_group_members(group_id)` | Membership |
| `add_user_group(user_id, group_id)` / `remove_user_group(user_id, group_id)` | Assign / remove |
| `delete_group(group_id)` | Delete group |

## Other

```python
idp.get_identity_providers()   # List configured IdPs
idp.token_is_valid(token)      # Check JWT validity
idp.open_id_configuration      # OIDC discovery document
```

## Keycloak configuration

Minimum setup for this library — see [keycloak-configuration.md](references/keycloak-configuration.md).

**Realm**: enabled, OpenID endpoint configuration, user registration if needed.

**App client**: enabled, Direct Access Grants (password flow), Service Accounts,
Authorization enabled. Set **Valid Redirect URIs** to your `callback_uri`.

**`admin-cli` client**: access type confidential, Service Accounts enabled, Full
Scope Allowed. **Service Account Roles**: all client roles from `account` and
`realm_management`. Without this, `FastAPIKeycloak` raises `AssertionError` on
startup.

## Exceptions

| Exception | When |
|-----------|------|
| `KeycloakError` | Admin API or token exchange failed (`status_code`, `reason`) |
| `UserNotFound` | `get_user` found no match |
| `MandatoryActionException` | Password login blocked by required action |
| `VerifyEmailException`, `ConfigureTOTPException`, … | Specific required actions |
| `HTTPException` | Invalid JWT or missing role in `get_current_user` |

Keycloak often returns `{"error": "unknown_error"}` — check Keycloak server logs
for details.

## Local dev stack

See [examples/quickstart_app.py](examples/quickstart_app.py) and
[references/docker-compose.yaml](references/docker-compose.yaml). Keycloak on
`:8085`, FastAPI on `:8081`. Admin UI: `keycloakuser` / `keycloakpassword`.

On Apple Silicon, if the stock Keycloak image fails to start, rebuild the image
locally — see [references/apple-m1.md](references/apple-m1.md).

## Additional resources

- Full API method signatures: [references/api-reference.md](references/api-reference.md)
- Keycloak client/realm checklist: [references/keycloak-configuration.md](references/keycloak-configuration.md)
- Upstream docs: https://github.com/fastapi-keycloak/fastapi-keycloak/tree/main/documentation
