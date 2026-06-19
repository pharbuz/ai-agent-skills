# Users, sessions, visits & beacons

Identify users, attach session-level properties, inspect captured metadata, and
control session/visit lifecycle and beacon sending.

A **visit** is a stretch of activity; it times out after inactivity, after which
a new visit ID is generated. A **beacon** is the payload RUM sends to Dynatrace.

Contents: [identifyUser](#identifyuser) · [sendSessionProperties](#sendsessionproperties) ·
[getAndEvaluateMetaData](#getandevaluatemetadata) · [endSession](#endsession) ·
[sendBeacon](#sendbeacon) · [now](#now) ·
[addVisitTimeoutListener](#addvisittimeoutlistener) ·
[addPageLeavingListener](#addpageleavinglistener)

---

### identifyUser

```typescript
identifyUser(value: string): void
```

Sets the
[user tag](https://www.dynatrace.com/support/help/shortlink/user-tagging#user-tagging-via-javascript-api),
which is used to identify individual users across different browsers, devices,
and sessions.

**Parameters:**

- `value`: `string` — The username. This can be a name, user ID, or email address.

**Returns:** `void`

---

### sendSessionProperties

```typescript
sendSessionProperties(
    javaLongOrObject?: PropertyObject | PropertyMap<number>,
    date?: PropertyMap<Date>,
    shortString?: PropertyMap<string>,
    javaDouble?: PropertyMap<number>,
): PropertiesSendingReport
```

Sends [session properties](https://www.dynatrace.com/support/help/shortlink/user-session-properties)
on a beacon. Currently only accepts valid java long, java double (as a string
representation), `Date` objects, and short strings of a maximum length of
100–1000 characters (as configured under Application Settings).

NOTE: session properties need to have a **lower case key**. Make sure to first
define session properties under Application settings before making this API call.

The first argument can either be a `PropertyObject` (carrying all four typed maps
at once — see [types.md](types.md)) **or** the java-long map directly followed by
the other typed maps.

**Parameters:**

- `javaLongOrObject` _(optional)_: `PropertyObject | PropertyMap<number>` — Either a `PropertyObject`, or key-value pairs of valid integers (range -9223372036854776000 to 9223372036854776000).
- `date` _(optional)_: `PropertyMap<Date>` — Key-value pairs of JavaScript `Date` objects.
- `shortString` _(optional)_: `PropertyMap<string>` — Key-value pairs of strings, each less than 100 characters.
- `javaDouble` _(optional)_: `PropertyMap<number>` — Key-value pairs of valid floating point numbers (range -1.7976931348623157e+308 to 1.7976931348623157e+308).

**Returns:** `PropertiesSendingReport` — A status report about the properties: failed properties (with reason), successfully sent properties, and a summary of total failures. See [types.md](types.md).

**See:** `addActionProperties` is related and works similarly (per-action instead of per-session).

---

### getAndEvaluateMetaData

```typescript
getAndEvaluateMetaData(): MetaData[]
```

Retrieves and evaluates metadata for the page, which can be used for
troubleshooting RUM monitoring.

**Returns:** `MetaData[]` — An array of metadata objects, each containing an id, type, expression, the captured value, and an optional failure reason. See [types.md](types.md).

---

### endSession

```typescript
endSession(): void
```

Immediately ends the current session.

**Returns:** `void`

---

### sendBeacon

```typescript
sendBeacon(
    forceSync: boolean,
    sendPreview: boolean,
    killUnfinished: boolean,
): void
```

Forces the sending of a beacon to ensure actions are not lost. For example, use
this method before a window unload event by adding an `addPageLeavingListener`.

**Parameters:**

- `forceSync`: `boolean` — DEPRECATED: This parameter is not used anymore and has no effect if provided.
- `sendPreview`: `boolean` — Forces the sending of preview beacons containing actions that have not yet been closed.
- `killUnfinished`: `boolean` — Terminates unfinished actions and sends them immediately. Handle with care, as actions might be inaccurate.

**Returns:** `void`

**See:** `addPageLeavingListener`

---

### now

```typescript
now(): number
```

Returns the current time in milliseconds using the most accurate method
available. Use this to produce `startTime`/`stopTime` values consistent with what
RUM uses internally.

**Returns:** `number` — The current time in milliseconds.

---

### addVisitTimeoutListener

```typescript
addVisitTimeoutListener(
    listener: (visitId: string, newVisitAfterTimeout: boolean) => void,
): void
```

Adds a listener that is triggered when the current visit times out and before a
new visit ID is generated.

**Parameters:**

- `listener`: `(visitId: string, newVisitAfterTimeout: boolean) => void` — Receives the timed-out visit ID and a boolean indicating whether a new visit will start due to timeout.

**Returns:** `void`

---

### addPageLeavingListener

```typescript
addPageLeavingListener(listener: (unloadRunning: boolean) => void): void
```

Adds a listener that is called when the user is leaving the page, before the RUM
monitoring beacon is sent. Use this method to hook into the page unload event.

**Parameters:**

- `listener`: `(unloadRunning: boolean) => void` — Called when the user leaves the page. `unloadRunning` is `true` if the page is currently being dismissed.

**Returns:** `void`
