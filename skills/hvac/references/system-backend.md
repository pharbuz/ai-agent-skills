# hvac — System backend (`client.sys`)

The system backend is Vault's operational / admin plane: cluster lifecycle,
mounts, policies, leases, audit devices, namespaces, and token administration.

## Init, seal & unseal

```python
client.sys.is_initialized()                                   # bool

# one-time initialization — returns unseal keys + the initial root token
result = client.sys.initialize(secret_shares=5, secret_threshold=3)
keys, root_token = result["keys"], result["root_token"]       # also result["keys_base64"]
client.token = root_token

# unseal — submit `threshold` keys (one at a time, or all at once)
client.sys.is_sealed()
client.sys.submit_unseal_key(keys[0])
client.sys.submit_unseal_keys(keys[:3])                       # batch
client.sys.read_seal_status()

client.sys.seal()                                             # re-seal (needs the right policy)
```

A **sealed** Vault rejects secret operations with `VaultDown` (503). Auto-unseal
(cloud KMS) skips manual key submission.

## Health & status

```python
client.sys.read_health_status(method="GET")     # standby/active/sealed/version
client.sys.read_leader_status()
client.sys.read_seal_status()
```

## Secrets engine mounts

```python
client.sys.enable_secrets_engine(backend_type="kv", path="apps", options={"version": "2"})
client.sys.list_mounted_secrets_engines()
client.sys.tune_mount_configuration(path="apps", default_lease_ttl="30m", max_lease_ttl="24h")
client.sys.read_mount_configuration(path="apps")
client.sys.move_backend(from_path="apps", to_path="services")
client.sys.disable_secrets_engine(path="apps")
```

## Auth method mounts

```python
client.sys.enable_auth_method(method_type="approle", path="approle")
client.sys.list_auth_methods()
client.sys.tune_auth_method(path="approle", default_lease_ttl="1h")
client.sys.disable_auth_method(path="approle")
```

## ACL policies

```python
policy = '''
path "secret/data/myapp/*" {
  capabilities = ["read"]
}
path "secret/metadata/myapp/*" {
  capabilities = ["list"]
}
'''
client.sys.create_or_update_policy(name="app-ro", policy=policy)
client.sys.list_policies()["data"]["policies"]
client.sys.read_policy(name="app-ro")["data"]["rules"]
client.sys.delete_policy(name="app-ro")
```

Policy strings are HCL. With `pip install "hvac[parser]"` you can pass parsed
policy objects, but a plain HCL string is the common path. Remember KV v2 splits
data (`secret/data/...`) from metadata/list (`secret/metadata/...`).

## Leases (dynamic secrets)

```python
client.sys.read_lease(lease_id=lease_id)
client.sys.renew_lease(lease_id=lease_id, increment=3600)     # extend TTL (seconds)
client.sys.revoke_lease(lease_id=lease_id)                    # revoke now
client.sys.revoke_prefix(prefix="database/creds/readonly")    # revoke all under a prefix
```

## Token administration

Token *creation*/*lookup* is under `client.auth.token`; broad token admin is here:

```python
client.auth.token.create(policies=["app-ro"], ttl="1h", renewable=True)
client.auth.token.lookup(token=some_token)
client.auth.token.revoke(token=some_token)
client.auth.token.revoke_and_orphan_children(token=some_token)   # revoke, keep children
```

## Audit devices

```python
client.sys.enable_audit_device(device_type="file", options={"file_path": "/var/log/vault_audit.log"})
client.sys.list_enabled_audit_devices()
client.sys.disable_audit_device(path="file")
```

## Response wrapping / unwrapping

Wrap a response in a single-use token (e.g. to hand a `secret_id` to an app
without exposing it in transit), then unwrap it once:

```python
# wrap: pass wrap_ttl on the originating call (most methods accept it), e.g.
wrapped = client.auth.approle.generate_secret_id(role_name="my-app", wrap_ttl="60s")
wrapping_token = wrapped["wrap_info"]["token"]

# unwrap (single use; errors if already used or expired)
secret_id = client.sys.unwrap(token=wrapping_token)["data"]["secret_id"]

# or wrap an arbitrary payload yourself (single-use token, ttl in seconds)
wrap_token = client.sys.wrap(payload={"k": "v"}, ttl=60)["wrap_info"]["token"]
```

## Enterprise namespaces

```python
client.sys.create_namespace(path="team-a")
client.sys.list_namespaces()
client.sys.delete_namespace(path="team-a")
# operate inside a namespace by constructing the client with namespace="team-a"
# (or set client.adapter.namespace) — all paths become relative to it.
```

---

## Notes

- **Capabilities are policy-gated.** Most `sys` operations (seal, mounts,
  policies, audit) require a token with `sudo`/admin capabilities — expect
  `Forbidden` (403) with an under-privileged token.
- **`read_health_status` codes.** Standby/uninitialized/sealed states map to
  non-200 HTTP codes by design; pass `method="GET"` (or `"HEAD"`) and read the
  returned JSON rather than treating non-200 as a hard failure.
- **KV v2 in policies** needs the `data/`/`metadata/` segments that client calls
  omit — the single most common cause of an unexpected `Forbidden`.
