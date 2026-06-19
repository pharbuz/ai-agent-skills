# Privacy, consent & session replay

Use these methods to integrate RUM with a user-consent / cookie-banner tool. In
**opt-in mode**, RUM starts disabled; enable it only after consent and disable it
(clearing cookies) on revocation. Persistent values control monitoring of
returning users; session replay can be toggled independently.

Contents: [enable](#enable) · [disable](#disable) ·
[enablePersistentValues](#enablepersistentvalues) ·
[disablePersistentValues](#disablepersistentvalues) ·
[enableSessionReplay](#enablesessionreplay) ·
[disableSessionReplay](#disablesessionreplay)

---

### enable

```typescript
enable(): void
```

Enables RUM JavaScript if it was previously disabled via the
[opt-in mode](https://www.dynatrace.com/support/help/shortlink/configure-rum-privacy#opt-in-mode).
Use this method in conjunction with a user consent tool to enable RUM monitoring
once consent has been provided.

**Returns:** `void`

**See:** `disable`

---

### disable

```typescript
disable(): void
```

Disables RUM JavaScript and removes all cookies if it was previously enabled with
`enable`, thereby activating the
[opt-in mode](https://www.dynatrace.com/support/help/shortlink/configure-rum-privacy#opt-in-mode).
Use this method along with a user consent tool to disable RUM monitoring when
consent is not provided.

**Returns:** `void`

**See:** `enable`

---

### enablePersistentValues

```typescript
enablePersistentValues(): void
```

Re-enables persistent values if they were previously disabled by calling
`disablePersistentValues`. Use this method when you want to resume monitoring
returning users.

**Returns:** `void`

---

### disablePersistentValues

```typescript
disablePersistentValues(remember: boolean): void
```

Removes all persistent values and disables any functionality that would recreate
them. Note that this must be called on **every page**, as it erases persistent
RUM monitoring data, including the information that prevents persistent data from
being stored.

Use this method when you want to disable monitoring of returning users. For more
information, see
[cookie storage](https://www.dynatrace.com/support/help/shortlink/cookies#cookie-storage).

**Parameters:**

- `remember`: `boolean` — If `true`, the configuration state is saved in local storage so that it persists across page loads.

**Returns:** `void`

---

### enableSessionReplay

```typescript
enableSessionReplay(ignoreCostControl: boolean): void
```

Enables session replay.

**Parameters:**

- `ignoreCostControl`: `boolean` — If `true`, enables session replay regardless of the cost control configuration.

**Returns:** `void`

---

### disableSessionReplay

```typescript
disableSessionReplay(): void
```

Disables session replay.

**Returns:** `void`
