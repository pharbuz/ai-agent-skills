# Keycloak sample configuration

## Create a new realm

1. **General**: Enabled, OpenID Endpoint Configuration
2. **Login**: User registration enabled

## Create a new client

1. **Settings**: Enabled, Direct Access Granted, Service Accounts Enabled, Authorization Enabled
2. **Scope**: Full Scope Allowed (will automatically grant all available roles to all users using this client; you may want to disable this and assign roles to the client manually)
3. **Valid Redirect URIs**: `http://localhost:8081/callback` (or whatever you configure in your Python app)

## Modify the `admin-cli` client

1. **Settings**: Access Type confidential, Service Accounts Enabled
2. **Scope**: Full Scope Allowed
3. **Service Account Roles**: Select all Client Roles available for `account` and `realm_management`

The `FastAPIKeycloak` constructor calls `_get_admin_token()` on startup. The admin
token must include `resource_access` for `account` and `realm-management` (or
`master-realm` on Keycloak 26+). Misconfiguration surfaces as:

```
AssertionError: The access required was not contained in the access token for the `admin-cli`.
Possibly a Keycloak misconfiguration. Check if the admin-cli client has `Full Scope Allowed`
and that the `Service Account Roles` contain all roles from `account` and `realm_management`
```
