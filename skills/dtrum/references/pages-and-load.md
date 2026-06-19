# Pages & load lifecycle

Two related concerns:

- **Page detection** — what RUM calls the current "view". In single-page apps,
  switch to manual detection and call `setPage` on each route change so views
  aren't all lumped under the initial URL.
- **Load-end timing** — when the load action is considered finished. Frameworks
  that keep loading after `DOMContentLoaded` can take over load-end signaling so
  the load action duration reflects real readiness.

Contents: [setPage](#setpage) · [enableManualPageDetection](#enablemanualpagedetection) ·
[enableAutomaticPageDetection](#enableautomaticpagedetection) ·
[markAsErrorPage](#markaserrorpage) · [setLoadEndManually](#setloadendmanually) ·
[signalLoadEnd](#signalloadend) · [incrementOnLoadEndMarkers](#incrementonloadendmarkers) ·
[signalOnLoadStart](#signalonloadstart) · [signalOnLoadEnd](#signalonloadend)

---

### setPage

```typescript
setPage(newPage: { group?: string; name: string }): number
```

Starts a new page view and reports it to the Dynatrace server.

**Parameters:**

- `newPage`: `{ group?: string; name: string }` — `name` is the view name. `group` is the view group; include dynamic placeholders rather than concrete IDs — for the view name `"/books/123"`, use a group like `"books/:bookId"`. If `group` is null/undefined, the Dynatrace server calculates the group based on the name.

**Returns:** `number` — A negative number if starting the new page failed, or a positive number if the new page was started successfully.

---

### enableManualPageDetection

```typescript
enableManualPageDetection(): void
```

Enables manual page detection. Once this method is called, RUM JavaScript stops
automatically detecting page and page group names and only uses the values
provided via `setPage`. It is recommended to call this as early as possible. To
resume automatic detection, call `enableAutomaticPageDetection`.

**Returns:** `void`

---

### enableAutomaticPageDetection

```typescript
enableAutomaticPageDetection(): void
```

Re-enables automatic page detection after manual detection was enabled via
`enableManualPageDetection`. Once this method is called, RUM JavaScript resumes
automatically detecting page and page group names.

**Returns:** `void`

---

### markAsErrorPage

```typescript
markAsErrorPage(responseCode: number, message: string): boolean
```

Reports the HTTP status code and a custom message for the response of the current
page. For example, use this method to mark your 404 pages that respond with an
HTTP status code of 200. This method must be called **before the page's onload
event finishes**; otherwise the information is discarded.

**Parameters:**

- `responseCode`: `number` — The HTTP status code to set.
- `message`: `string` — An additional informational message.

**Returns:** `boolean` — `false` if the values were incorrect or the method was called too late; otherwise `true`.

---

### setLoadEndManually

```typescript
setLoadEndManually(): void
```

Prevents RUM JavaScript from automatically detecting the load end event. The load
end event must then be explicitly set using `signalLoadEnd`. Call this method
**immediately after injecting RUM JavaScript**.

**Returns:** `void`

---

### signalLoadEnd

```typescript
signalLoadEnd(): void
```

Signals that the page has finished loading. Use in combination with
`setLoadEndManually` to define your own load end times.

**Returns:** `void`

**See:** `setLoadEndManually`

---

### incrementOnLoadEndMarkers

```typescript
incrementOnLoadEndMarkers(): void
```

Instructs RUM JavaScript to wait for an additional call to `signalOnLoadEnd`
before closing the 'onload' action. Note: the load action will only use the
provided load end event correctly if `signalOnLoadEnd` is called afterward.

**Returns:** `void`

**See:** `setLoadEndManually`

---

### signalOnLoadStart

```typescript
signalOnLoadStart(): void
```

Indicates the start of a load action. Frameworks often have their own load
callback functions, and this method can be used when a framework begins loading
before the 'DOMContentLoaded' event.

**Returns:** `void`

---

### signalOnLoadEnd

```typescript
signalOnLoadEnd(): void
```

Indicates the end of a load action. This method requires that
`incrementOnLoadEndMarkers` has been called beforehand. The action is closed
after the final call to `signalOnLoadEnd`.

**Returns:** `void`

**See:** `signalOnLoadStart`
