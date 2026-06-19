---
name: dtrum
description: >-
  Use the Dynatrace RUM `dtrum` JavaScript API (the global `window.dtrum` object
  injected by Dynatrace Real User Monitoring / OneAgent) to manually instrument
  browser apps. Trigger WHENEVER the user works with `dtrum`, `window.dtrum`, or
  the Dynatrace RUM Classic JavaScript API — creating custom user actions
  (`enterAction`/`leaveAction`), instrumenting XHR/fetch or single-page-app
  navigations, tagging users (`identifyUser`), reporting errors
  (`reportError`/`reportCustomError`), sending session or action properties,
  controlling page detection (`setPage`, manual vs automatic), managing
  load-end timing for SPAs, privacy opt-in/consent (`enable`/`disable`,
  persistent values), or session replay. Also trigger on Dynatrace RUM
  instrumentation in JavaScript/TypeScript, SPA action tracking, manual web
  instrumentation, "dtrum is undefined", or wiring user actions into Angular/
  React/Vue. Covers all 41 dtrum methods, signatures, supporting types, and
  instrumentation patterns.
---

# dtrum — Dynatrace RUM Classic JavaScript API

`dtrum` is the global JavaScript object that the **Dynatrace RUM JavaScript**
(injected automatically by OneAgent, or added as a manual agent snippet) exposes
on `window`. It is the *Classic* RUM API — the full control surface for **manual
instrumentation** of Real User Monitoring: custom user actions, XHR/async
actions, page detection for single-page apps, error reporting, user tagging,
session/action properties, privacy/consent, and session replay.

Official reference: <https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html>

> This skill mirrors the full `dtrum` type reference (41 methods + supporting
> types) scraped from the Dynatrace JavaScript API docs. For the exact signature,
> parameters, return value, and notes of any method, open the linked reference
> file — every method is documented there verbatim.

## When you need this skill

You usually only call `dtrum` when **automatic detection isn't enough**:
single-page apps where navigations and async calls aren't auto-captured, custom
business actions, consent-gated monitoring, or enriching beacons with your own
user/session/action properties. For a standard multi-page app, OneAgent's
automatic instrumentation already captures actions, XHRs, and errors — reach for
`dtrum` to *correct*, *extend*, or *replace* that behavior.

## Loading & availability — guard every call

The RUM JavaScript is injected asynchronously, so `window.dtrum` may not exist
yet (or at all, if monitoring is disabled or blocked). **Never assume it's
present** — guard every call so your app never throws when monitoring is absent:

```javascript
if (window.dtrum) {
  window.dtrum.identifyUser("user@example.com");
}

// Reusable helper
function rum(fn) {
  if (window.dtrum) {
    try { return fn(window.dtrum); } catch (e) { /* never let RUM break the app */ }
  }
}
rum((dt) => dt.reportError(new Error("checkout failed")));
```

`dtrum` is the advanced/full API. Dynatrace also exposes a smaller `dynatrace`
convenience object for the most common calls; when you need the methods below,
use `dtrum`.

## Mental model — actions are the core unit

RUM groups user interactions into **user actions** (Load, XHR, or custom). Most
of the API is about opening, naming, extending, and closing actions:

1. **Actions are identified by a numeric ID.** Every `enter*` method *returns* an
   ID; you pass that ID to the matching `leave*`/`mark*` method. `0` or a negative
   number signals failure.
2. **Open → (work) → close.** `enterAction(name)` → … → `leaveAction(id)`. An
   action that is never left is closed automatically (or on beacon send), which
   can produce inaccurate durations — always pair them.
3. **Automatic detection is ON by default.** Call
   `setAutomaticActionDetection(false)` to instrument fully manually, or hook the
   auto-created actions with enter/leave **listeners** instead of replacing them.
4. **Times are epoch milliseconds.** Optional `startTime`/`stopTime` args let you
   backdate, but a start time more than an hour in the past is ignored.
5. **Properties & user context ride along on the beacon** — `identifyUser`,
   `addActionProperties`, `sendSessionProperties` attach metadata to the current
   action/session/visit.

```javascript
// Custom action lifecycle
var actionId = dtrum.enterAction("Add to cart");
// ... do the work ...
dtrum.leaveAction(actionId);
```

## Method groups → reference files

Open the file for the group you need. Each lists every method with its exact
signature, parameters, return value, deprecations, and `@see` cross-references.

| Group | Reference | Methods |
|-------|-----------|---------|
| Custom & automatic **actions**, naming, listeners, action properties | [`references/actions.md`](references/actions.md) | `enterAction`, `leaveAction`, `actionName`, `setAutomaticActionDetection`, `addEnterActionListener`, `removeEnterActionListener`, `addLeaveActionListener`, `removeLeaveActionListener`, `addActionProperties` |
| **XHR / async actions** & manual user input | [`references/xhr-and-input.md`](references/xhr-and-input.md) | `enterXhrAction`, `leaveXhrAction`, `enterXhrCallback`, `leaveXhrCallback`, `markXHRFailed`, `beginUserInput`, `endUserInput` |
| **Pages & load lifecycle** (SPA page detection, load-end timing, error pages) | [`references/pages-and-load.md`](references/pages-and-load.md) | `setPage`, `enableManualPageDetection`, `enableAutomaticPageDetection`, `markAsErrorPage`, `setLoadEndManually`, `signalLoadEnd`, `incrementOnLoadEndMarkers`, `signalOnLoadStart`, `signalOnLoadEnd` |
| **Error reporting** | [`references/errors.md`](references/errors.md) | `reportError`, `reportCustomError` |
| **Users, sessions, visits & beacons** | [`references/sessions-and-users.md`](references/sessions-and-users.md) | `identifyUser`, `sendSessionProperties`, `getAndEvaluateMetaData`, `endSession`, `sendBeacon`, `now`, `addVisitTimeoutListener`, `addPageLeavingListener` |
| **Privacy, consent & session replay** | [`references/privacy-and-consent.md`](references/privacy-and-consent.md) | `enable`, `disable`, `enablePersistentValues`, `disablePersistentValues`, `enableSessionReplay`, `disableSessionReplay` |
| **Supporting types** (enums, interfaces, property maps) | [`references/types.md`](references/types.md) | `ActionNameResult`, `DtRumUserInput`, `MetaData`, `PropertiesSendingReport`, `FailedProperty`, `SuccessfulProperty`, `PropertyObject`, `PropertyMap` |

## Common patterns

### Custom action with properties

```javascript
var id = dtrum.enterAction("Submit order");
// ... order logic ...
// keys must be lowercase and pre-defined under Application Settings
dtrum.addActionProperties(id, { itemcount: 3 }, null, { coupon: "SUMMER" });
dtrum.leaveAction(id);
```

### Instrument an async XHR/fetch the agent won't auto-link

```javascript
// mode 1 = extend any running action; pass the URL so it isn't logged as "/undefined"
var xhrId = dtrum.enterXhrAction("fetch", 1, "/api/products");
fetch("/api/products")
  .then((res) => {
    if (!res.ok) dtrum.markXHRFailed(res.status, "products fetch failed", xhrId);
  })
  .finally(() => dtrum.leaveXhrAction(xhrId));
```

### Single-page-app navigation (manual page detection)

```javascript
dtrum.enableManualPageDetection();            // stop auto page naming (call early)
router.afterEach((to) => {
  dtrum.setPage({ name: to.path, group: to.matched[0]?.path }); // e.g. "books/:bookId"
});
```

### Tag the user and report a caught error

```javascript
dtrum.identifyUser("user@example.com");        // user tag across sessions/devices
try {
  doRiskyThing();
} catch (e) {
  dtrum.reportError(e);                         // propagate caught errors to Dynatrace
}
```

### Consent-gated monitoring (opt-in mode)

```javascript
// In opt-in mode RUM starts disabled. Enable after consent, disable on revoke.
consent.onGranted(() => dtrum.enable());
consent.onRevoked(() => dtrum.disable());       // also clears cookies
```

### Flush before the page unloads

```javascript
dtrum.addPageLeavingListener(function () {
  dtrum.sendBeacon(false, true, true);          // send preview + kill unfinished actions
});
```

## Gotchas & deprecations

- **`dtrum` may be `undefined`** — always guard (see above). The single most
  common error is "dtrum is undefined" from calling before injection / when
  monitoring is off.
- **IDs, not handles.** `enter*` returns a number; keep it and pass it to the
  matching `leave*`. Don't share IDs across actions.
- **Lowercase, pre-defined property keys.** `addActionProperties` /
  `sendSessionProperties` only accept keys you've defined under *Application
  Settings*, and the key must be lowercase, or the property is dropped (check the
  returned [`PropertiesSendingReport`](references/types.md)).
- **Value-type buckets matter.** Properties are split by type: java-long ints,
  java-double floats (as strings), `Date` objects, and short strings
  (100–1000 chars). Put each value in the correct argument slot.
- **Deprecated parameters (still in signatures, ignored):** `enterAction`'s
  `actionType`, and `sendBeacon`'s `forceSync`. Pass anything / leave them.
- **Timing rules.** `markAsErrorPage` must run before the page's onload finishes;
  `markXHRFailed` before the XHR action closes; a `leaveAction` `startTime` more
  than an hour in the past is ignored.
- **Manual load-end is sticky.** After `setLoadEndManually()` the load action
  won't close until you call `signalLoadEnd()` — forgetting it leaves the action
  open.

## Updating this skill

Reference files are generated from the Dynatrace JavaScript API TypeDoc pages
(static HTML — no JS rendering needed, so plain `curl` + `jsdom` parsing works).
See [`scripts/scrape_dtrum_docs.md`](scripts/scrape_dtrum_docs.md) for the
approach (fetch `doc/types/dtrum.html` + linked interface/enum pages, parse each
`section.tsd-member` for name/signature/description/params/returns).
