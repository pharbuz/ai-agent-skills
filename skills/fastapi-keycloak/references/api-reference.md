# FastAPIKeycloak API reference

## Constructor

```python
FastAPIKeycloak(
    server_url: str,           # Keycloak URL with /auth suffix
    client_id: str,
    client_secret: str,
    realm: str,
    admin_client_secret: str,
    callback_uri: str,
    admin_client_id: str = "admin-cli",
    scope: str = "openid profile email",
    timeout: int = 10,
    ssl_verification: bool = True,
    algorithms: str | Container[str] | None = None,
)
```

## FastAPI integration

| Method / property | Returns | Description |
|-------------------|---------|-------------|
| `add_swagger_config(app)` | `None` | PKCE OAuth config for Swagger UI |
| `user_auth_scheme` | `OAuth2PasswordBearer` | Auth scheme (cached) |
| `get_current_user(required_roles=None, extra_fields=None)` | `Callable` | FastAPI dependency → `OIDCUser` |

## Auth & tokens

| Method / property | Returns | Description |
|-------------------|---------|-------------|
| `user_login(username, password)` | `KeycloakToken` | Password grant |
| `exchange_authorization_code(session_state, code)` | `KeycloakToken` | Authorization code grant |
| `refresh_token(refresh_token)` | `KeycloakToken` | Refresh grant |
| `token_is_valid(token, audience=None)` | `bool` | Validate JWT |
| `login_uri` | `str` | Full authorization redirect URL |
| `logout_uri` | `str` | End-session endpoint |
| `token_uri` | `str` | Token endpoint |
| `authorization_uri` | `str` | Authorization endpoint |
| `open_id_configuration` | `dict` | OIDC discovery |
| `public_key` | `str` | PEM public key for JWT verify |

## Users

| Method | Returns |
|--------|---------|
| `create_user(first_name, last_name, username, email, password, enabled=True, initial_roles=None, send_email_verification=True, attributes=None)` | `KeycloakUser` |
| `get_user(user_id=None, query="")` | `KeycloakUser` |
| `get_all_users()` | `List[KeycloakUser]` |
| `update_user(user)` | `KeycloakUser` |
| `delete_user(user_id)` | `dict` |
| `change_password(user_id, new_password, temporary=False)` | `dict` |
| `send_email_verification(user_id)` | `dict` |

## Roles

| Method | Returns |
|--------|---------|
| `create_role(role_name)` | `KeycloakRole` |
| `get_all_roles()` | `List[KeycloakRole]` |
| `get_roles(role_names)` | `List[KeycloakRole]` |
| `get_user_roles(user_id)` | `List[KeycloakRole]` |
| `add_user_roles(roles, user_id)` | `dict` |
| `remove_user_roles(roles, user_id)` | `dict` |
| `delete_role(role_name)` | `dict` |

## Groups

| Method | Returns |
|--------|---------|
| `create_group(group_name, parent=None)` | `KeycloakGroup` |
| `get_all_groups()` | `List[KeycloakGroup]` |
| `get_groups(group_names)` | `List[KeycloakGroup]` |
| `get_group(group_id)` | `KeycloakGroup` |
| `get_group_by_path(path, search_in_subgroups=True)` | `KeycloakGroup` |
| `get_user_groups(user_id)` | `List[KeycloakGroup]` |
| `get_group_members(group_id)` | `List[KeycloakUser]` |
| `add_user_group(user_id, group_id)` | `dict` |
| `remove_user_group(user_id, group_id)` | `dict` |
| `delete_group(group_id)` | `dict` |

## Other

| Method | Returns |
|--------|---------|
| `get_identity_providers()` | `List[KeycloakIdentityProvider]` |

## Models

| Class | Purpose |
|-------|---------|
| `OIDCUser` | Decoded access token; `.roles` property |
| `KeycloakUser` | Admin API user representation |
| `KeycloakToken` | `access_token`, `refresh_token`, `id_token` |
| `KeycloakRole` | Realm role |
| `KeycloakGroup` | Group (supports `subGroups`) |
| `KeycloakIdentityProvider` | External IdP config |
| `UsernamePassword` | Pydantic body for password login (`SecretStr` password) |
| `HTTPMethod` | `GET`, `POST`, `PUT`, `DELETE` enum |

## Exceptions

| Class | Base |
|-------|------|
| `KeycloakError` | `Exception` |
| `UserNotFound` | `Exception` |
| `MandatoryActionException` | `HTTPException` |
| `UpdateUserLocaleException` | `MandatoryActionException` |
| `ConfigureTOTPException` | `MandatoryActionException` |
| `VerifyEmailException` | `MandatoryActionException` |
| `UpdatePasswordException` | `MandatoryActionException` |
| `UpdateProfileException` | `MandatoryActionException` |
