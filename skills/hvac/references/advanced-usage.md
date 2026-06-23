# hvac — Advanced usage & integration

`hvac` is **synchronous** (built on `requests`). There is no official async
client; for async apps run hvac calls in a thread executor
(`await asyncio.to_thread(client.secrets.kv.v2.read_secret_version, path=...)`).

## Retries with a custom `requests.Session`

Vault API calls should retry on transient/eventual-consistency errors. Build a
`Session` with a `urllib3` `Retry` and pass it to the client:

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import hvac

adapter = HTTPAdapter(max_retries=Retry(
    total=3,
    backoff_factor=0.1,                       # delay = backoff * (2 ** (n-1))
    status_forcelist=[412, 500, 502, 503],    # 412 = eventual-consistency replay
    raise_on_status=False,                    # let hvac raise its own exceptions
))
session = requests.Session()
session.mount("http://", adapter)
session.mount("https://", adapter)

client = hvac.Client(url="https://vault.example.com", session=session)
```

- **`raise_on_status=False` is important** — it lets hvac surface its own
  `VaultError` subclasses consistently instead of urllib3 raising first.
- **`status_forcelist`** — include `412` for performance-standby/eventual
  consistency; `5xx` for transient server issues.
- **`allowed_methods`** — by default POST/PATCH are **not** retried (they aren't
  idempotent). Add them only when you understand the write semantics.

## TLS with a private CA

```python
client = hvac.Client(url="https://vault.example.com", verify="/etc/ssl/my-ca-bundle.pem")

# or via the session
session = requests.Session()
session.verify = "/etc/ssl/my-ca-bundle.pem"
client.session = session
```

Combine the system trust store with a custom CA:

```bash
cp "$(python -c 'import certifi; print(certifi.where())')" /tmp/bundle.pem
cat /path/to/custom-ca.pem >> /tmp/bundle.pem
# then verify="/tmp/bundle.pem"
```

Prefer pointing `verify` at a CA bundle over `verify=False`; disabling
verification exposes you to MITM and only belongs in throwaway dev.

## Vault Agent — unix socket listener

Talk to a local Vault Agent over a unix socket (the agent handles auth/renewal
for you), using `requests_unixsocket`:

```python
import urllib.parse, requests_unixsocket, hvac

socket_path = "/var/run/vault/agent.sock"
socket_url = "http+unix://" + urllib.parse.quote(socket_path, safe="")
client = hvac.Client(url=socket_url, session=requests_unixsocket.Session())
```

## Custom adapters

The client uses `hvac.adapters.JSONAdapter` by default (parses JSON responses).
Pass a different adapter to change transport/parsing behavior:

```python
from hvac.adapters import RawAdapter
client = hvac.Client(url=url, token=tok, adapter=RawAdapter)   # returns raw requests.Response
```

Subclass `hvac.adapters.Adapter` and override its request methods for full
control (custom auth headers, logging, instrumentation).

## Raw / unsupported endpoints

hvac doesn't wrap every Vault endpoint. Drop to the adapter for raw HTTP — paths
are relative to `/v1`:

```python
client.adapter.get("/v1/sys/health")
client.adapter.post("/v1/secret/data/myapp", json={"data": {"k": "v"}})
client.adapter.put("/v1/...", json={...})
client.adapter.delete("/v1/...")
client.adapter.list("/v1/secret/metadata/myapp")              # LIST verb
```

The default `JSONAdapter` returns the parsed dict; `RawAdapter` returns the
`requests.Response`.

## Namespaces (Enterprise)

```python
client = hvac.Client(url=url, token=tok, namespace="team-a/app")
# every path is now relative to the namespace; or switch at runtime:
client.adapter.namespace = "team-b"
```

## Integration patterns

A small factory + injected wrapper keeps Vault out of your business logic and
makes testing easy (mirrors how you'd inject any client):

```python
import os, hvac

def build_vault_client() -> hvac.Client:
    client = hvac.Client(url=os.environ["VAULT_ADDR"])
    client.auth.approle.login(
        role_id=os.environ["VAULT_ROLE_ID"],
        secret_id=os.environ["VAULT_SECRET_ID"],
    )
    if not client.is_authenticated():
        raise RuntimeError("Vault authentication failed")
    return client

class SecretStore:
    def __init__(self, client: hvac.Client, mount_point: str = "secret") -> None:
        self._c, self._mp = client, mount_point

    def get(self, path: str) -> dict:
        resp = self._c.secrets.kv.v2.read_secret_version(
            path=path, mount_point=self._mp, raise_on_deleted_version=True,
        )
        return resp["data"]["data"]
```

- **Token expiry in long-lived processes.** Tokens have a TTL; renew with
  `client.auth.token.renew_self()` before expiry, or re-`login()` on
  `Forbidden`/`Unauthorized`. For zero-touch renewal, front your app with Vault
  Agent (above) and read tokens/secrets it writes.
- **Testing.** Inject a fake/`Mock` `hvac.Client` into `SecretStore`; or run a
  `vault server -dev` instance and point `VAULT_ADDR`/`VAULT_TOKEN` at it for
  integration tests.
- **Thread safety.** A `Client` wraps a `requests.Session`; share one per process
  for read-heavy workloads, but don't mutate `client.token`/`namespace`
  concurrently from multiple threads — give each principal/namespace its own
  client.
