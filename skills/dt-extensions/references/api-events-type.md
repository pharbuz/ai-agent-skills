# Event Type (DtEventType enum)

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/api/events/event_type.html

The `DtEventType` enum defines event types for **Events v2 ingest API**. Used
only with `Extension.report_dt_event()` and `report_dt_event_dict()`.

```python
from dynatrace_extension import DtEventType

self.report_dt_event(
    DtEventType.CUSTOM_ALERT,
    "High CPU on host",
    entity_selector='type("HOST"),entityId("HOST-123")',
    properties={"cpu": "95"},
)
```

Official API: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/events-v2/post-event

## Class

```python
class dynatrace_extension.DtEventType(value)
```

Event type for Events v2 ingestion.

## Members

| Member | Value | Description |
|--------|-------|-------------|
| `DtEventType.AVAILABILITY_EVENT` | `'AVAILABILITY_EVENT'` | Availability problem |
| `DtEventType.CUSTOM_INFO` | `'CUSTOM_INFO'` | Informational custom event |
| `DtEventType.CUSTOM_ALERT` | `'CUSTOM_ALERT'` | Custom alert (can open problem) |
| `DtEventType.CUSTOM_ANNOTATION` | `'CUSTOM_ANNOTATION'` | Annotation on entity |
| `DtEventType.CUSTOM_CONFIGURATION` | `'CUSTOM_CONFIGURATION'` | Configuration change |
| `DtEventType.CUSTOM_DEPLOYMENT` | `'CUSTOM_DEPLOYMENT'` | Deployment event |
| `DtEventType.ERROR_EVENT` | `'ERROR_EVENT'` | Error event |
| `DtEventType.MARKED_FOR_TERMINATION` | `'MARKED_FOR_TERMINATION'` | Entity marked for termination |
| `DtEventType.PERFORMANCE_EVENT` | `'PERFORMANCE_EVENT'` | Performance degradation |
| `DtEventType.RESOURCE_CONTENTION_EVENT` | `'RESOURCE_CONTENTION_EVENT'` | Resource contention |

## report_dt_event_dict schema

When using `report_dt_event_dict(event)` instead of `report_dt_event()`:

```python
{
    "eventType": "CUSTOM_ALERT",   # required — one of enum values above
    "title": "...",                # required, min length 1
    "startTime": 1699993566909,    # optional, UTC ms
    "endTime": 1699997166909,      # optional, UTC ms
    "timeout": 15,                 # optional, minutes
    "entitySelector": 'type("HOST")',  # optional
    "properties": {"key": "value"},    # optional, all values strings
}
```
