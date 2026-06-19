# Error reporting

OneAgent automatically captures uncaught JavaScript errors via the global
`onerror` handler. Use these methods for errors your code **catches and handles**
(which therefore never reach `onerror`) and for **custom business errors** such
as form-validation failures.

See also `markXHRFailed` in [xhr-and-input.md](xhr-and-input.md) for flagging
failed requests.

Contents: [reportError](#reporterror) · [reportCustomError](#reportcustomerror)

---

### reportError

```typescript
reportError(error: string | Error, parentActionId?: number): void
```

Reports an error to Dynatrace. Use this method when you catch errors in your
application code and want to propagate them to Dynatrace, rather than handling
them solely with your own logging. If the error is managed by your application,
it will not be handled by the global JavaScript
[onerror event handler](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onerror),
which Dynatrace uses to automatically capture JavaScript errors.

**Parameters:**

- `error`: `string | Error` — The error to report. Any standard browser error object is supported. If the error does not include a stack trace, the RUM JavaScript will attempt to generate one. Alternatively, provide your own object with these properties: `message` (required), `file`, `line`, `column`, and `stack` (all optional).
- `parentActionId` _(optional)_: `number` — The parent action ID. If not provided or null, the error is added to the current action.

**Returns:** `void`

---

### reportCustomError

```typescript
reportCustomError(
    key: string,
    value: string,
    hint?: string,
    parentingInfo?: number | boolean,
): void
```

Reports [custom errors](https://www.dynatrace.com/support/help/shortlink/configure-application-errors#configure-custom-errors)
to Dynatrace. Use this method to capture custom errors, such as form validation
errors, that are defined in Application settings.

**Parameters:**

- `key`: `string` — The key of the error (e.g., 'validation error').
- `value`: `string` — The error value (e.g., 'Email validation failed').
- `hint` _(optional)_: `string` — An optional hint to identify the issue, such as the content of the input element that triggered the error.
- `parentingInfo` _(optional)_: `number | boolean` — Defines how the custom error should be attached. When a **number** is provided, the error is attached to the specified open action. When a **boolean** `true` is provided, it is attached to the currently active action.

**Returns:** `void`
