# Metric Type (MetricType enum)

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/api/metrics/metric_type.html

Two metric categories can be sent to Dynatrace:

- **Gauge** — single value that can go up or down (e.g. current CPU %)
- **Counter** — continuously increasing value (e.g. bytes received since start)

Used with `Extension.report_metric()` and `Metric` constructor.

```python
from dynatrace_extension import MetricType

self.report_metric("requests.total", 1, metric_type=MetricType.COUNT)
self.report_metric("cpu.usage", 42.5, metric_type=MetricType.GAUGE)
self.report_metric("errors.delta", 3, metric_type=MetricType.DELTA)
```

## Class

```python
class dynatrace_extension.MetricType(value)
```

An enumeration.

## Members

| Member | MINT value | Description |
|--------|------------|-------------|
| `MetricType.GAUGE` | `'gauge'` | Default. Point-in-time value |
| `MetricType.COUNT` | `'count'` | Monotonically increasing counter |
| `MetricType.DELTA` | `'count,delta'` | Counter reported as delta since last report |

## When to use each type

| Type | Example metrics |
|------|-----------------|
| `GAUGE` | CPU %, memory used, queue depth, temperature |
| `COUNT` | Total requests, total bytes transferred |
| `DELTA` | Requests in last interval, bytes since last poll |
