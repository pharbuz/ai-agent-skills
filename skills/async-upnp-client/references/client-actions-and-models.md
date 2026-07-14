# Client Actions And Models

## Create A Device

```python
from async_upnp_client.aiohttp import AiohttpSessionRequester
from async_upnp_client.client_factory import UpnpFactory

requester = AiohttpSessionRequester(session)
factory = UpnpFactory(requester, non_strict=True)
device = await factory.async_create_device(description_url)
```

Use `non_strict=True` for real-world devices with imperfect XML. Keep strict
mode for tests and controlled devices.

## UpnpDevice

Important fields/properties:

- `device_info`, `name`, `friendly_name`, `manufacturer`, `model_name`, `udn`
- `device_type`, `device_url`, `presentation_url`, `icons`, `xml`
- `services`, `embedded_devices`, `all_devices`, `all_services`
- `ssdp_headers`, `available`, `parent_device`, `root_device`

Lookups:

```python
device.find_device(device_type)
device.find_service(service_type)
device.service(service_type)
device.service_id(service_id)
device.has_service(service_type)
```

`async_ping()` checks whether the description can still be fetched.

## UpnpService

Important fields/properties:

- `service_type`, `service_id`, `control_url`, `event_sub_url`, `scpd_url`
- `state_variables`, `actions`, `device`, `xml`

Action calls:

```python
result = await service.async_call_action("GetVolume", InstanceID=0, Channel="Master")
```

Metadata:

```python
action = service.action("GetVolume")
var = service.state_variable("Volume")
```

`notify_changed_state_variables(changes)` updates evented state variables and
fires the service event callback.

## UpnpAction

Important methods:

- `validate_arguments(**kwargs)`
- `in_arguments()`
- `out_arguments()`
- `argument(name, direction=None)`
- `async_call(**kwargs)`
- `create_request(**kwargs)`
- `parse_response(service_type, http_response)`

The action validates input against related `UpnpStateVariable` schemas and
raises library exceptions for bad values, SOAP faults, or HTTP errors.

## UpnpStateVariable

Important fields/properties:

- `name`, `data_type`, `default_value`, `send_events`
- `min_value`, `max_value`, `step_value`, `allowed_values`
- `value`, `value_unchecked`, `upnp_value`, `updated_at`
- `coerce_python(upnp_value)`, `coerce_upnp(value)`, `validate_value(value)`

State variable type mapping covers UPnP types such as `ui4`, `i4`, `string`,
`boolean`, `dateTime`, `time.tz`, `uri`, `uuid`, and numeric float types.

## Hooks

`UpnpFactory` accepts hooks for fixing odd devices:

- `on_pre_receive_device_spec`
- `on_post_receive_device_spec`
- `on_pre_receive_service_spec`
- `on_post_receive_service_spec`
- `on_pre_call_action`
- `on_post_call_action`

Use hooks for controlled normalization such as trimming invalid trailing bytes,
adding headers, or logging SOAP traffic.
