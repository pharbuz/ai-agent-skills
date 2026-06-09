# Authentication

dt-async supports two credential types. **Which one you pass to `DynatraceAsync`
decides which `dt.<service>` accessors exist.** Reaching for a service that your
credentials don't support raises a clear `AttributeError` telling you to switch.

## DynatraceOAuthCredentials (OAuth 2.0 client credentials)

```python
from dynatrace import DynatraceAsync, DynatraceOAuthCredentials

dt = DynatraceAsync(
    base_url="https://abc12345.apps.dynatrace.com",
    credentials=DynatraceOAuthCredentials(
        client_id="dt0s02.SAMPLE",
        client_secret="dt0s02.SAMPLE.abcd...",
        account_uuid="00000000-0000-0000-0000-000000000000",
        scope="storage:entities:read storage:metrics:read",  # space-separated
        sso_base_url="https://sso.dynatrace.com",             # default
    ),
)
```

Frozen dataclass fields:

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `client_id` | yes | — | OAuth client id (`dt0s02...`) |
| `client_secret` | yes | — | OAuth client secret |
| `account_uuid` | yes | — | Your Dynatrace account UUID |
| `scope` | no | `"account-uac-read"` | Space-separated scopes; must cover every API you call |
| `sso_base_url` | no | `"https://sso.dynatrace.com"` | SSO token endpoint host |

How it works under the hood (authlib `AsyncOAuth2Client`):

- Grant type `client_credentials`; token endpoint `{sso_base_url}/sso/oauth2/token`.
- The `resource` is `urn:dtaccount:{account_uuid}`.
- The token is fetched lazily and **auto-refreshed** when expired or on a `401`
  (the request is retried once after refresh).

**Unlocks:** `dt.platform.*` (Grail/DQL, Davis, AppEngine registry) and
`dt.account.*` (IAM, subscriptions, audits, notifications) — plus all the
Environment V2 services.

## DynatraceAccessToken (API token)

```python
from dynatrace import DynatraceAsync, DynatraceAccessToken

dt = DynatraceAsync(
    base_url="https://abc12345.live.dynatrace.com",
    credentials=DynatraceAccessToken(token="dt0c01.SAMPLE.abcd..."),
)
```

Sends `Authorization: Api-Token <token>` on every request. **Unlocks:**
Environment **V1** and **Configuration V1** services (e.g. `dt.dashboards`,
`dt.plugins`, `dt.timeseries`, `dt.management_zones`, `dt.alerting_profiles`) —
plus all Environment V2 services.

## Which services each credential type exposes

**Available with BOTH** (Environment API V2 + common):
`activegates`, `activegates_autoupdate_configuration`,
`activegates_autoupdate_jobs`, `activegates_remote_configuration`, `audit_logs`,
`custom_tags`, `entities`, `events_v2`, `extensions_v2`, `logs`, `metrics`,
`management_zones_v2`, `network_zones`, `oneagents_remote_configuration`,
`problems`, `security_problems`, `settings`, `slos`, `synthetic_monitors_v2`,
`tenant_tokens`, `tokens`, `credentials`.

**API token only** (Environment V1 + Configuration V1) — these raise
`AttributeError` under OAuth:
`cluster_time`, `custom_devices`, `deployment`, `events`, `oneagents`,
`smartscape_hosts`, `synthetic_monitors`, `third_part_synthetic_tests`,
`timeseries`, `alerting_profiles`, `anomaly_detection_metric_events`,
`anomaly_detection_process_groups`, `auto_tags`, `dashboards`, `extensions`,
`maintenance_windows`, `management_zones`, `notifications`,
`oneagents_config_environment`, `oneagents_config_host`,
`oneagents_config_hostgroup`, `plugins`, `config_v1`.

**OAuth only** — these raise `AttributeError` under an API token:
`platform` (and everything under it), `account` (and everything under it).

> If you need both Config-V1 *and* Platform APIs in one workflow, create **two
> clients** — one per credential type — rather than trying to share one.

## Choosing the base URL

| You are calling… | base_url |
|------------------|----------|
| Platform APIs (Grail/DQL, AppEngine) | `https://<envId>.apps.dynatrace.com` |
| Classic environment APIs (V1/V2, SaaS) | `https://<envId>.live.dynatrace.com` |
| Managed cluster | `https://<cluster>/e/<envId>` |
| Account Management API | `https://api.dynatrace.com` |

Trailing slashes on `base_url` are trimmed automatically.

## Scopes (OAuth)

The `scope` string must include every permission the called APIs require, joined
by spaces. Common values:

- Account/IAM: `account-uac-read`, `account-env-read`, `iam:users:read`, …
- Grail storage: `storage:entities:read`, `storage:metrics:read`,
  `storage:logs:read`, `storage:events:read`, `storage:buckets:read`
- Settings/automation as needed: `settings:objects:read`, `settings:objects:write`

A `403` almost always means the scope (OAuth) or token permissions (API token)
don't cover the endpoint — widen them.

## Constructor validation & extras

- `base_url` is required (raises `ValueError` if empty).
- OAuth requires `client_id`, `client_secret`, `account_uuid`; token requires
  `token` (each raises `ValueError` if missing).
- `mc_jsession_id` / `mc_b925d32c` / `mc_sso_csrf_cookie` set internal Dynatrace
  Mission Control cookies — only for that niche; ignore for normal tenant use.
- `verify_ssl` defaults to **`False`**. Set `verify_ssl=True` in production.
