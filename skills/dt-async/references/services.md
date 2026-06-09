# Service catalogue

Every accessor hangs off the `DynatraceAsync` client as `dt.<service>`. Methods
are coroutines (`await`); `list()`-style methods return async-iterable
`PaginatedList`s. Grouping below also tells you the **credential type** required
(see [authentication.md](authentication.md)).

Legend: ✅ implemented · ⚠️ partial coverage.

## Environment API V2 — available with OAuth *and* API token

| API | Accessor | |
|-----|----------|---|
| Access tokens (API tokens) | `dt.tokens` | ✅ |
| Access tokens (tenant tokens) | `dt.tenant_tokens` | ✅ |
| ActiveGates | `dt.activegates` | ✅ |
| ActiveGates – auto-update config | `dt.activegates_autoupdate_configuration` | ✅ |
| ActiveGates – auto-update jobs | `dt.activegates_autoupdate_jobs` | ✅ |
| ActiveGates – remote configuration | `dt.activegates_remote_configuration` | ✅ |
| Audit logs | `dt.audit_logs` | ✅ |
| Events | `dt.events_v2` | ✅ |
| Extensions 2.0 | `dt.extensions_v2` | ✅ |
| Logs | `dt.logs` | ✅ |
| Metrics | `dt.metrics` | ✅ |
| Monitored entities | `dt.entities` | ✅ |
| Monitored entities – custom tags | `dt.custom_tags` | ✅ |
| Network zones | `dt.network_zones` | ✅ |
| OneAgents – remote configuration | `dt.oneagents_remote_configuration` | ✅ |
| Problems | `dt.problems` | ✅ |
| Security problems | `dt.security_problems` | ✅ |
| Service-level objectives | `dt.slos` | ✅ |
| Settings 2.0 | `dt.settings` | ✅ |
| Settings – management zones | `dt.management_zones_v2` | ✅ |
| Synthetic – monitors | `dt.synthetic_monitors_v2` | ✅ |
| Credential vault | `dt.credentials` | ✅ |

## Environment API V1 — API token only

| API | Accessor | |
|-----|----------|---|
| Cluster time | `dt.cluster_time` | ✅ |
| Custom devices | `dt.custom_devices` | ✅ |
| Deployment | `dt.deployment` | ✅ |
| Events | `dt.events` | ⚠️ |
| OneAgent on a host | `dt.oneagents` | ⚠️ |
| Synthetic – monitors | `dt.synthetic_monitors` | ⚠️ |
| Synthetic – third party | `dt.third_part_synthetic_tests` | ✅ |
| Timeseries | `dt.timeseries` | ⚠️ |
| Smartscape – hosts | `dt.smartscape_hosts` | ⚠️ |
| Smartscape – custom device | `dt.custom_devices` | ⚠️ |

## Configuration API V1 — API token only

| API | Accessor | |
|-----|----------|---|
| Alerting profiles | `dt.alerting_profiles` | ⚠️ |
| Anomaly detection – metric events | `dt.anomaly_detection_metric_events` | ⚠️ |
| Anomaly detection – process groups | `dt.anomaly_detection_process_groups` | ⚠️ |
| Automatically applied tags | `dt.auto_tags` | ⚠️ |
| Custom tags | `dt.custom_tags` | ✅ |
| Dashboards | `dt.dashboards` | ⚠️ |
| Extensions (v1) | `dt.extensions` | ✅ |
| Maintenance windows | `dt.maintenance_windows` | ⚠️ |
| Management zones | `dt.management_zones` | ⚠️ |
| Notifications | `dt.notifications` | ⚠️ |
| OneAgent – environment-wide config | `dt.oneagents_config_environment` | ✅ |
| OneAgent in a host group | `dt.oneagents_config_hostgroup` | ✅ |
| OneAgent on a host | `dt.oneagents_config_host` | ✅ |
| Plugins | `dt.plugins` | ⚠️ |
| Configuration V1 (aggregate) | `dt.config_v1` | ✅ |

## Platform API — OAuth only (`dt.platform.*`)

| API | Accessor | |
|-----|----------|---|
| AppEngine – Registry (apps, schema manifest) | `dt.platform.appengine_registry` | ✅ |
| Davis CoPilot | `dt.platform.davis_copilot` | ✅ |
| Davis AI – predictive & causal analyzers | `dt.platform.davis_analyzers` | ⚠️ |
| DQL query – execution | `dt.platform.grail_query_execution` | ✅ |
| DQL query – assistance | `dt.platform.grail_query_assistance` | ✅ |

DQL execution methods: `execute(query, ...)` → `QueryStartResponse`;
`poll(request_token, ...)` → `QueryPollResponse`; `cancel(request_token, ...)`.
See [usage-patterns.md](usage-patterns.md#dql--grail).

## Account API — OAuth only (`dt.account.*`)

| API | Accessor | |
|-----|----------|---|
| User management | `dt.account.iam_users` | ✅ |
| Group management | `dt.account.iam_groups` | ✅ |
| Permission & policy management | `dt.account.iam_policies` | ✅ |
| Service user management | `dt.account.iam_service_users` | ✅ |
| Platform tokens | `dt.account.iam_platform_tokens` | ✅ |
| Environment management v1 / v2 | `dt.account.env_v1` / `dt.account.env_v2` | ✅ |
| Subscription management | `dt.account.sub_v2`, `dt.account.sub_v3` | ✅ |
| Subscription – rate cards | `dt.account.sub_v1_rate_cards` | ✅ |
| Subscription – cost allocation | `dt.account.sub_v1_cost_allocation` | ✅ |
| Account audits | `dt.account.audits` | ✅ |
| Account notifications | `dt.account.notifications` | ✅ |

## Finding a service's methods

The accessors map to service classes in the `dynatrace/` package; method names
mirror the REST API (`list`, `get`, `create`/`post`, `update`/`put`, `delete`).
When unsure of arguments, inspect the service class or use the live API docs at
<https://www.dynatrace.com/support/help/dynatrace-api>. Endpoints are defined as
`ENDPOINT_*` constants on each service class.
