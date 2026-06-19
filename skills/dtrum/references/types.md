# Supporting types

Enums, interfaces, and the property-map type used by the `dtrum` methods.

Contents: [ActionNameResult](#actionnameresult-enum) · [DtRumUserInput](#dtrumuserinput) ·
[MetaData](#metadata) · [PropertiesSendingReport](#propertiessendingreport) ·
[FailedProperty](#failedproperty) · [SuccessfulProperty](#successfulproperty) ·
[PropertyObject](#propertyobject) · [PropertyMap](#propertymap)

---

### ActionNameResult (enum)

Provides information about the result of a call to `dtrum.actionName`.

```typescript
enum ActionNameResult {
  SUCCESS = 0,             // the action name was updated
  ACTION_NOT_FOUND = 1,    // no matching/active action
  INVALID_ACTION_NAME = 2, // the provided name was invalid
  INVALID_ACTION_ID = 3,   // the provided action ID was invalid
}
```

---

### DtRumUserInput

Returned by `beginUserInput`; passed back to `endUserInput`.

```typescript
interface DtRumUserInput {
  info: string;                    // additional info supplied when the input began
  name: string;                    // the resulting action caption
  target: string | EventTarget;    // the DOM node / identifier that triggered it
  title: string;
}
```

---

### MetaData

Returned (as an array) by `getAndEvaluateMetaData` — useful for troubleshooting
what RUM captured.

```typescript
interface MetaData {
  expression: string;  // the capture expression
  type: string;        // the metadata type
  value: string;       // the captured value
  info?: string;       // optional failure reason / extra info
}
```

---

### PropertiesSendingReport

Returned by `addActionProperties` and `sendSessionProperties`. Inspect this to
find out which properties were dropped (e.g. undefined key under Application
Settings, wrong type, or too long) and why.

```typescript
interface PropertiesSendingReport {
  failedProperties: FailedProperty[];     // properties that were not sent, with reasons
  sentProperties: SuccessfulProperty[];   // properties accepted
  info: string;                           // summary message (e.g. total failures)
}
```

---

### FailedProperty

```typescript
interface FailedProperty {
  key: string;     // the property key that failed
  reason: string;  // why it was rejected
}
```

---

### SuccessfulProperty

```typescript
interface SuccessfulProperty {
  key: string;
  value: string | number | Date;
}
```

---

### PropertyObject

A single object bundling all four typed property maps — accepted as the first
argument of `sendSessionProperties` instead of passing the maps positionally.

```typescript
interface PropertyObject {
  javaLong?: PropertyMap<number>;    // integer values
  javaDouble?: PropertyMap<number>;  // floating-point values
  date?: PropertyMap<Date>;          // Date values
  shortString?: PropertyMap<string>; // short string values (<100 chars)
}
```

---

### PropertyMap

A keyed map of property values of one type. In practice you pass a plain object
literal whose **keys are lowercase** and pre-defined under Application Settings.

```typescript
type PropertyMap<S extends string | number | Date> = {
  [key: string]: S | Property<S>;
};

// Usage — just a plain object:
dtrum.sendSessionProperties({ accountid: 4711 }, { signupdate: new Date() });
//                          ^ PropertyMap<number>  ^ PropertyMap<Date>
```

Each value type goes in its own argument slot on `addActionProperties` /
`sendSessionProperties`: integers → `javaLong`, floats → `javaDouble`, dates →
`date`, short strings → `shortString`.
