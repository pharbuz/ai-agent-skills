# Event Severity (Severity enum)

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/api/events/event_severity.html

The `Severity` class defines severity of a **log-ingest event**. Used only with
`Extension.report_event()`.

```python
from dynatrace_extension import Severity

self.report_event(
    "Title", "Description",
    severity=Severity.ERROR,
)
```

## Class

```python
class dynatrace_extension.Severity(value)
```

Severity of an event ingested through log ingest.

## Members

| Member | Value | Typical use |
|--------|-------|-------------|
| `Severity.EMERGENCY` | `'EMERGENCY'` | System unusable |
| `Severity.ERROR` | `'ERROR'` | Error conditions |
| `Severity.ALERT` | `'ALERT'` | Immediate action required |
| `Severity.CRITICAL` | `'CRITICAL'` | Critical conditions |
| `Severity.SEVERE` | `'SEVERE'` | Severe conditions |
| `Severity.WARN` | `'WARN'` | Warning conditions |
| `Severity.NOTICE` | `'NOTICE'` | Normal but significant |
| `Severity.INFO` | `'INFO'` | Informational (default) |
| `Severity.DEBUG` | `'DEBUG'` | Debug-level messages |

`severity` parameter also accepts plain strings matching the values above.
