# Actions — custom, automatic, listeners & properties

User **actions** are the core unit of RUM. Use these methods to create custom
actions, rename them, switch off automatic detection, hook into auto-created
actions with listeners, and attach custom properties.

Lifecycle: `var id = dtrum.enterAction(name)` → … → `dtrum.leaveAction(id)`.
Every `enter*` returns a numeric **action ID** (`0` = not created); pass it to
the matching `leave*`/property method.

Contents: [enterAction](#enteraction) · [leaveAction](#leaveaction) ·
[actionName](#actionname) · [setAutomaticActionDetection](#setautomaticactiondetection) ·
[addEnterActionListener](#addenteractionlistener) ·
[removeEnterActionListener](#removeenteractionlistener) ·
[addLeaveActionListener](#addleaveactionlistener) ·
[removeLeaveActionListener](#removeleaveactionlistener) ·
[addActionProperties](#addactionproperties)

---

### enterAction

```typescript
enterAction(
    actionName: string,
    actionType?: string,
    startTime?: number,
    sourceUrl?: string,
): number
```

Enters a new custom action. Use this method to create a custom action. This
method must be called before `leaveAction`, which closes the custom action.

**Parameters:**

- `actionName`: `string` — The name of the action.
- `actionType` _(optional)_: `string` — DEPRECATED: This parameter is not used anymore and has no effect if provided.
- `startTime` _(optional)_: `number` — The timestamp in milliseconds. If falsy, the current time is used.
- `sourceUrl` _(optional)_: `string` — The source URL for the action.

**Returns:** `number` — The ID of the created action, or 0 if the action was not created.

**See:** `leaveAction`

---

### leaveAction

```typescript
leaveAction(actionId: number, stopTime?: number, startTime?: number): void
```

Leaves an action that was previously created using `enterAction`. Use this method
to set the load end event for a custom action and complete its creation. This
method must be called after `enterAction`.

**Parameters:**

- `actionId`: `number` — The ID of the action to leave. This must be the value returned by `enterAction`.
- `stopTime` _(optional)_: `number` — The timestamp in milliseconds. Providing a stop time will force the action to stop and prevent the visually complete module from extending it.
- `startTime` _(optional)_: `number` — Optional start time in milliseconds (necessary if the start time should be modified). Note that the start time must not be more than an hour in the past; otherwise it is ignored.

**Returns:** `void`

**See:** `enterAction`

---

### actionName

```typescript
actionName(actionName: string, actionId?: number): ActionNameResult
```

Sets the name of the currently active action, or the action corresponding to the
provided ID.

**Parameters:**

- `actionName`: `string` — The new name for the action.
- `actionId` _(optional)_: `number` — The ID of the action to update. If omitted, the currently active action is updated.

**Returns:** `ActionNameResult` — An `ActionNameResult` indicating whether the update was successful. (See [types.md](types.md) — `SUCCESS`, `ACTION_NOT_FOUND`, `INVALID_ACTION_NAME`, `INVALID_ACTION_ID`.)

---

### setAutomaticActionDetection

```typescript
setAutomaticActionDetection(enabled: boolean): void
```

Enables or disables automatic action detection. Use this method when you want to
manually instrument your application.

**Parameters:**

- `enabled`: `boolean` — Specifies whether automatic action detection should be enabled or disabled.

**Returns:** `void`

**See:** `enterAction`, `leaveAction`

---

### addEnterActionListener

```typescript
addEnterActionListener(
    listener: (
        actionId: number,
        starttime: number,
        isRootAction: boolean,
        element?: string | EventTarget,
    ) => void,
): void
```

Attaches a listener that is called while entering an action.

Remove the listener if not needed, or filter actions using `addActionProperties`
to prevent sending the same action property for every action. Use this method to
hook into the automatic action creation event to influence related concepts such
as action naming or action properties.

**Parameters:**

- `listener`: `(actionId: number, starttime: number, isRootAction: boolean, element?: string | EventTarget) => void` — The callback triggered when an action is entered. Receives the action ID, start time, whether it is a root action, and the element that initiated the event.

**Returns:** `void`

**See:** `removeEnterActionListener`, `actionName`, `addActionProperties`

---

### removeEnterActionListener

```typescript
removeEnterActionListener(
    listener: (
        actionId: number,
        starttime: number,
        isRootAction: boolean,
        element?: string | EventTarget,
    ) => void,
): void
```

Removes a previously attached listener that detects the enter action event. Pass
the same function reference you registered with `addEnterActionListener`.

**Parameters:**

- `listener`: `(actionId, starttime, isRootAction, element?) => void` — The reference to the listener to be removed.

**Returns:** `void`

**See:** `addEnterActionListener`

---

### addLeaveActionListener

```typescript
addLeaveActionListener(
    listener: (
        actionId: number,
        stoptime: number,
        isRootAction: boolean,
    ) => void,
): void
```

Attaches a listener that is called when leaving an action.

Remove the listener if not needed, or filter actions using `addActionProperties`
to prevent sending the same action property for every action. Use this method to
hook into the out-of-the-box action closing event.

**Parameters:**

- `listener`: `(actionId: number, stoptime: number, isRootAction: boolean) => void` — The callback triggered when an action is left. Receives the action ID, end time, and whether it is a root action.

**Returns:** `void`

**See:** `removeLeaveActionListener`, `addActionProperties`

---

### removeLeaveActionListener

```typescript
removeLeaveActionListener(
    listener: (
        actionId: number,
        stoptime: number,
        isRootAction: boolean,
    ) => void,
): void
```

Removes a previously attached listener that detects the leave action event.

**Parameters:**

- `listener`: `(actionId, stoptime, isRootAction) => void` — The callback function to be removed.

**Returns:** `void`

**See:** `addLeaveActionListener`

---

### addActionProperties

```typescript
addActionProperties(
    parentActionId: number,
    javaLong?: PropertyMap<number>,
    date?: PropertyMap<Date>,
    shortString?: PropertyMap<string>,
    javaDouble?: PropertyMap<number>,
): PropertiesSendingReport
```

Adds custom [action properties](https://www.dynatrace.com/support/help/shortlink/user-session-properties)
to the currently active action.

Only accepts valid java long, java double (as a string representation), `Date`
objects, and short strings with a maximum length of 100–1000 characters (as
configured under Application Settings). Action properties must be defined under
Application settings and use a **lowercase key**.

**Parameters:**

- `parentActionId`: `number` — The ID of the action.
- `javaLong` _(optional)_: `PropertyMap<number>` — Key-value pairs of valid integers, in range -9223372036854776000 to 9223372036854776000.
- `date` _(optional)_: `PropertyMap<Date>` — Key-value pairs of JavaScript `Date` objects.
- `shortString` _(optional)_: `PropertyMap<string>` — Key-value pairs of strings, each less than 100 characters.
- `javaDouble` _(optional)_: `PropertyMap<number>` — Key-value pairs of valid floating point numbers, in range -1.7976931348623157e+308 to 1.7976931348623157e+308.

**Returns:** `PropertiesSendingReport` — A status report about the properties passed to the function: failed properties (with reason), successfully sent properties, and a summary of the total number of failures. See [types.md](types.md).

**See:** `sendSessionProperties`
