# XHR / async actions & manual user input

Use these methods when an XHR/fetch call or a user interaction isn't
automatically correlated with an action — common in single-page apps with
asynchronous data loading. XHR actions extend or start an action around a
request so it isn't closed prematurely (which would skew action duration).

Lifecycle: `var id = dtrum.enterXhrAction(type, mode, url)` → … →
`dtrum.leaveXhrAction(id)`. Use `markXHRFailed` to flag a logically-failed
request even when the HTTP status is 200.

Contents: [enterXhrAction](#enterxhraction) · [leaveXhrAction](#leavexhraction) ·
[enterXhrCallback](#enterxhrcallback) · [leaveXhrCallback](#leavexhrcallback) ·
[markXHRFailed](#markxhrfailed) · [beginUserInput](#beginuserinput) ·
[endUserInput](#enduserinput)

---

### enterXhrAction

```typescript
enterXhrAction(type: string, xmode?: 0 | 1 | 3, xhrUrl?: string): number
```

Extends or initiates actions. Use this method when you want to extend an active
Load or XHR action with an unlinked XHR call. It is particularly useful when the
XHR call is asynchronous and cannot be automatically correlated with an action,
which might otherwise cause the action to close prematurely, leading to
inaccurate metrics (such as user action duration). This method must be called
before `leaveXhrAction`.

**Parameters:**

- `type`: `string` — Optional information about the type of XHR (e.g., framework name).
- `xmode` _(optional)_: `0 | 1 | 3` — XHR action creation mode:
  - `0` — Extend only running XHR actions.
  - `1` — Extend any running action.
  - `3` — Start an action if a user input is present.
- `xhrUrl` _(optional)_: `string` — The URL of the requested resource. **Always provide this** — if omitted, the request appears as "/undefined" in the waterfall.

**Returns:** `number` — The ID of the XHR action.

**See:** `leaveXhrAction`

---

### leaveXhrAction

```typescript
leaveXhrAction(actionId: number, stopTime?: number): void
```

Indicates the end of an XHR action.

**Parameters:**

- `actionId`: `number` — The ID of the XHR action.
- `stopTime` _(optional)_: `number` — The stop time of the XHR action in milliseconds.

**Returns:** `void`

**See:** `enterXhrAction`

---

### enterXhrCallback

```typescript
enterXhrCallback(actionId: number): void
```

Indicates that an XHR callback is active (e.g., `XMLHttpRequest`
`onreadystatechange`) and links subsequently triggered XHR actions to this
callback. For example, if an XHR callback adds a script tag to your page and
triggers another XHR call, that call would not automatically be added to the
current action. Calling this method allows the subsequent XHR call to be linked
to its initial action. The XHR callback must be concluded with
`leaveXhrCallback`.

**Parameters:**

- `actionId`: `number` — The ID of the action to which the callback belongs.

**Returns:** `void`

---

### leaveXhrCallback

```typescript
leaveXhrCallback(actionId: number): void
```

Indicates the end of an XHR callback.

**Parameters:**

- `actionId`: `number` — The ID of the action to which the callback belongs.

**Returns:** `void`

**See:** `enterXhrCallback`

---

### markXHRFailed

```typescript
markXHRFailed(
    responseCode: number,
    message: string,
    parentActionId?: number,
): boolean
```

Reports the HTTP status code and an additional message for the response of the
current XHR action. For example, use this method when the HTTP status code of
your XHR response is 200, but the server's result indicates a failed request.
This method must be called before the XHR action finishes and all listeners have
been invoked.

**Parameters:**

- `responseCode`: `number` — The HTTP status code of the current XHR action.
- `message`: `string` — An additional informational message.
- `parentActionId` _(optional)_: `number` — The optional ID of the action to mark as failed. If not provided, the currently open action is used.

**Returns:** `boolean` — `false` if the values were incorrect or the method was called too late; otherwise `true`.

---

### beginUserInput

```typescript
beginUserInput(
    domNode: string | HTMLElement,
    type: string,
    addInfo?: string,
    validTime?: number,
): DtRumUserInput
```

Indicates the start of a user input. Every user input must be concluded by
calling `endUserInput`. RUM JavaScript checks for an active user input when an
XHR call or a page load occurs. If a user input is active, that input is marked
as having triggered the user action. Use this method when a user input is not
automatically detected by RUM JavaScript.

**Parameters:**

- `domNode`: `string | HTMLElement` — The DOM node (or a string identifier) that triggered the action (e.g., a button). Determines the caption for the resulting action.
- `type`: `string` — The type of action (e.g., 'click', 'keypress', 'scroll').
- `addInfo` _(optional)_: `string` — Optional additional information about the user input (e.g., key, mouse button, etc.).
- `validTime` _(optional)_: `number` — The duration (in milliseconds) for which this user input should remain valid.

**Returns:** `DtRumUserInput` — An object containing information about the user input (see [types.md](types.md)).

**See:** `endUserInput`

---

### endUserInput

```typescript
endUserInput(userInputObject: DtRumUserInput): void
```

Ends a user input that was started with `beginUserInput`.

**Parameters:**

- `userInputObject`: `DtRumUserInput` — The user input object returned by `beginUserInput`.

**Returns:** `void`
