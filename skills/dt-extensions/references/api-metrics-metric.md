# Metric class

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/api/metrics/metric.html

The `Metric` class constructs MINT-compliant metric objects. Mostly used
internally — extension code typically calls `Extension.report_metric()` instead.

When `report_metric()` is called, the SDK builds a `Metric` object and queues it
for sending to the environment.

## Class

```python
class dynatrace_extension.Metric(
    key: str,
    value: float | int | str | SummaryStat,
    dimensions: dict[str, str] | None = None,
    metric_type: MetricType = MetricType.GAUGE,
    timestamp: datetime | None = None,
)
```

| Parameter | Description |
|-----------|-------------|
| `key` | Metric key (MINT specification) |
| `value` | Numeric value or `SummaryStat` |
| `dimensions` | Dimension key-value pairs |
| `metric_type` | `MetricType.GAUGE` (default) |
| `timestamp` | Defaults to current time |

## Methods

### `to_mint_line() → str`

Convert metric to a MINT protocol string. Useful for debugging or building
custom MINT output before calling `report_mint_lines()`.

```python
from dynatrace_extension import Metric, MetricType

m = Metric("my.cpu.usage", 42.5, dimensions={"host": "web-01"}, metric_type=MetricType.GAUGE)
line = m.to_mint_line()
self.report_mint_lines([line])
```

### `validate() → bool`

Validate metric against MINT specification. Returns `True` if valid.

## Typical usage

Prefer the high-level API:

```python
self.report_metric("my.cpu.usage", 42.5, dimensions={"host": "web-01"})
```

Use `Metric` directly only when you need `to_mint_line()` or pre-validation.

See also: [`api-metrics-type.md`](api-metrics-type.md) for `MetricType` enum.
