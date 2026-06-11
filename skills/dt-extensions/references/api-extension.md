# Extension API

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/api/extension.html

Base class for Python EF2 extensions: `dynatrace_extension.Extension`

Subclass in `__main__.py` as `ExtensionImpl(Extension)`.

## Class

```python
class dynatrace_extension.Extension(*args, **kwargs)
```

Base class for Python extensions.

## Attributes & properties

### `logger`

Embedded logger object for the extension.

### `schedule_decorators: ClassVar[list[tuple[Callable, timedelta | int, tuple | None, ActivationType | None]]]`

Class-level list of schedule decorator registrations.

### `is_helper: bool` (property)

Internal property used by the EEC.

### `task_id: str` (property)

Internal property used by the EEC.

### `monitoring_config_id: str` (property)

Internal property used by the EEC. Unique identifier of the monitoring
configuration assigned to this extension instance.

### `techrule: str` (property)

Internal property used by the EEC.

### `enabled_feature_sets: dict[str, list[str]]` (property)

Map of enabled feature sets and corresponding metrics from `extension.yaml`.

### `enabled_feature_sets_names: list[str]` (property)

Names of enabled feature sets.

### `enabled_feature_sets_metrics: list[str]` (property)

List of all metric keys from enabled feature sets.

## Lifecycle methods

### `run()`

Launch the extension instance. Must be invoked once to start the extension.

If `--fastcheck` is set, runs in fastcheck mode. Otherwise starts the main loop
which periodically runs:

- Scheduled callbacks
- Heartbeat method
- Metrics publisher method

### `initialize()`

Callback when extension starts. Called once after arguments are parsed and
activation config is received. Use to set schedule frequency from user config:

```python
def initialize(self):
    self.schedule(self.my_method, timedelta(minutes=5))
```

### `query() → Any`

Callback executed every **60 seconds** by default. Optional override in subclass.
Always scheduled regardless of other `schedule()` calls.

### `on_shutdown()`

Called when extension exits after shutdown signal from EEC. Runs **before**
metrics are flushed to EEC.

### `fastcheck() → Status`

Callback for fastcheck mode. Only invoked for **remote** extensions. Not called
if `register_fastcheck()` was used. Return `Status` with optional message.

### `register_fastcheck(fast_check_callback: Callable[[ActivationConfig, str], Status])`

Register custom fastcheck callback. When registered, `fastcheck()` is **not** called.

## Scheduling

### `schedule(callback, interval, args=None, activation_type=None, offset_seconds=None) → None`

Schedule a method to run periodically in a **separate thread**. Callback is
immediately scheduled for first execution.

| Parameter | Description |
|-----------|-------------|
| `callback` | Method to invoke |
| `interval` | `timedelta` or `int` (seconds) between invocations |
| `args` | Optional tuple of arguments passed to callback |
| `activation_type` | `ActivationType.LOCAL` or `ActivationType.REMOTE` |
| `offset_seconds` | First-run offset in seconds; random if `None` |

## Metrics

### `report_metric(key, value, dimensions=None, techrule=None, timestamp=None, metric_type=MetricType.GAUGE, device_address=None) → None`

Report a metric via MINT protocol to EEC → tenant. Default type: gauge.

| Parameter | Description |
|-----------|-------------|
| `key` | Metric key (MINT specification) |
| `value` | `float`, `str`, `int`, or `SummaryStat` |
| `dimensions` | `dict[str, str]` |
| `device_address` | Address of monitored device/endpoint |
| `techrule` | Technology rule string from `self.techrule` setter |
| `timestamp` | Defaults to current time |
| `metric_type` | `MetricType.GAUGE` (default), `COUNT`, or `DELTA` |

### `report_mint_lines(lines: list[str]) → None`

Report raw MINT lines. Lines must comply with MINT format.

```python
self.report_mint_lines(["my_metric 1", "my_other_metric 2"])
```

## Events

### `report_event(title, description, properties=None, timestamp=None, severity=Severity.INFO, send_immediately=False) → None`

Report event via **log ingest**.

| Parameter | Description |
|-----------|-------------|
| `title` | Event title |
| `description` | Event description |
| `properties` | Extra event properties dict |
| `timestamp` | Defaults to current time |
| `severity` | `Severity` enum or str; default `Severity.INFO` |
| `send_immediately` | Skip batching if `True` |

See [`api-events-severity.md`](api-events-severity.md) for `Severity` values.

### `report_dt_event(event_type, title, start_time=None, end_time=None, timeout=None, entity_selector=None, properties=None) → None`

Report event via **Events v2 ingest API**. Can raise events or problems directly.

Unlike `report_event`, uses `DtEventType` enum.

| Parameter | Description |
|-----------|-------------|
| `event_type` | `DtEventType` (required) |
| `title` | Event title (required) |
| `start_time` | UTC ms; default current timestamp |
| `end_time` | UTC ms; default current + timeout |
| `timeout` | Minutes; default 15 |
| `entity_selector` | Default: environment entity |
| `properties` | `dict[str, str]` |

API ref: https://www.dynatrace.com/support/help/dynatrace-api/environment-api/events-v2/post-event

See [`api-events-type.md`](api-events-type.md) for `DtEventType` values.

### `report_dt_event_dict(event: dict)`

Report event via Events v2 API using a dict. Required keys: `eventType`, `title`.

Allowed `eventType` values: `CUSTOM_INFO`, `CUSTOM_ANNOTATION`,
`CUSTOM_CONFIGURATION`, `CUSTOM_DEPLOYMENT`, `MARKED_FOR_TERMINATION`,
`ERROR_EVENT`, `AVAILABILITY_EVENT`, `PERFORMANCE_EVENT`,
`RESOURCE_CONTENTION_EVENT`, `CUSTOM_ALERT`.

Optional: `startTime`, `endTime`, `timeout`, `entitySelector`, `properties`.

## Logs

### `report_log_event(log_event: dict, send_immediately=False)`

Report custom log event via log ingest.
Ref: https://www.dynatrace.com/support/help/shortlink/log-monitoring-log-data-ingestion

### `report_log_events(log_events: list[dict], send_immediately=False)`

Report list of custom log events.

### `report_log_lines(log_lines: list[str | bytes], send_immediately=False)`

Report list of log lines via log ingest.

## Config & helpers

### `get_activation_config() → ActivationConfig`

Activation configuration for this extension instance.

### `get_version() → str`

Extension version string.

### `get_snapshot(snapshot_file: Path | str | None = None) → Snapshot`

Retrieve OneAgent snapshot. `snapshot_file` path only used with `dt-sdk run`.

### `get_fields_dimensions(endpoint: dict) → dict`

Parse `primaryFields` from endpoint dict → `{key: value}` dimensions.

### `get_tags_dimensions(endpoint: dict) → dict`

Parse `primaryTags` from endpoint dict → `{key: value}` dimensions.

### `get_tags_and_fields_dimensions(endpoint: dict) → dict`

Merged dimensions from `primaryFields` and `primaryTags`.

## Self-monitoring

EEC automatically sends `dsfm:datasource.python.*` metrics (execution time,
thread count, ok/timeout/exception counts). Visible in `dt-sdk run` output on
shutdown — not reported manually.
