# Forms

Strato design-system components in the **Forms** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## Checkbox

`/design/components/forms/Checkbox/`

Checkboxes allow the user to select one or more options from a list of options.

### Import

`tsx
import { Checkbox } from '@dynatrace/strato-components/forms';
`

### Use cases

#### Variants

The checkbox can be in either of the following states: `checked`, `unchecked`,
or `indeterminate`, shown in this example.

```tsx
import { Checkbox } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex gap={8} flexDirection="column">
      <Flex gap={8}>
        <Checkbox name="uncontrolled-unchecked">Unchecked</Checkbox>
        <Checkbox name="uncontrolled-checked" defaultValue>
          Checked
        </Checkbox>
        <Checkbox
          name="uncontrolled-indeterminate"
          defaultValue="indeterminate"
        >
          Indeterminate
        </Checkbox>
      </Flex>
      <Flex gap={8}>
        <Checkbox name="uncontrolled-unchecked" disabled>
          Unchecked
        </Checkbox>
        <Checkbox name="uncontrolled-checked" defaultValue disabled>
          Checked
        </Checkbox>
        <Checkbox
          name="uncontrolled-indeterminate"
          defaultValue="indeterminate"
          disabled
        >
          Indeterminate
        </Checkbox>
      </Flex>
    </Flex>
  );
};
```

```tsx
import { Checkbox } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex gap={8} flexDirection="column">
      <Flex gap={8}>
        <Checkbox name="uncontrolled-unchecked">Unchecked</Checkbox>
        <Checkbox name="uncontrolled-checked" defaultValue>
          Checked
        </Checkbox>
        <Checkbox
          name="uncontrolled-indeterminate"
          defaultValue="indeterminate"
        >
          Indeterminate
        </Checkbox>
      </Flex>
      <Flex gap={8}>
        <Checkbox name="uncontrolled-unchecked" disabled>
          Unchecked
        </Checkbox>
        <Checkbox name="uncontrolled-checked" defaultValue disabled>
          Checked
        </Checkbox>
        <Checkbox
          name="uncontrolled-indeterminate"
          defaultValue="indeterminate"
          disabled
        >
          Indeterminate
        </Checkbox>
      </Flex>
    </Flex>
  );
};
```


#### Control the state

The checkbox can also be controlled, meaning that you can handle the state. To
do so, you need to use the `onChange` prop to provide a handler that is called
when the internal state of the checkbox changes. You also need to assign the
value from the state to the checkbox by setting the `checked` prop.

#### Validate

This example shows how you can validate the checkbox using the `react-hook-form`
package, which handles error messages. For connecting the form with the checkbox
and validating, you need to register the field with custom error messages and
use the `useForm` hook from `react-hook-form`. Also, by using the `controlState`
prop, you can connect the checkbox's error state and message to that of the
form. This shows a hint in case of an error and applies proper styling to the
component.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Variants
- Control the state
- Validate

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import { Checkbox, FieldSet } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    'T&C': boolean;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <FieldSet>
            <FieldSet.Legend>Terms and conditions:</FieldSet.Legend>
            <Controller
              name="T&C"
              control={control}
              rules={{
                required: {
                  value: true,
                  message: 'Terms and conditions are required',
                },
              }}
              render={({ field, fieldState: { error } }) => (
                <Checkbox
                  formValue="checked"
                  required
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                >
                  I agree to the terms and conditions
                </Checkbox>
              )}
            />
          </FieldSet>
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import { Checkbox, FieldSet } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    'T&C': boolean;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <FieldSet>
            <FieldSet.Legend>Terms and conditions:</FieldSet.Legend>
            <Controller
              name="T&C"
              control={control}
              rules={{
                required: {
                  value: true,
                  message: 'Terms and conditions are required',
                },
              }}
              render={({ field, fieldState: { error } }) => (
                <Checkbox
                  formValue="checked"
                  required
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                >
                  I agree to the terms and conditions
                </Checkbox>
              )}
            />
          </FieldSet>
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Props

Checkboxes allow the user to select one or more options from a list of options.

#### CheckboxProps

##### Signature:
`export declare type CheckboxProps = ) => | > & & & & & & & {
 /**
 * A representing the value used for the checkbox.
 * When submitted in a form, it is only submitted if checked, with the set value.
 * If , the is submitted by default as per https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox#attr-value.
 */
 formValue?: ;
};`Still have questions?Find answers in the Dynatrace Community

---

## DateTimePicker

`/design/components/forms/DateTimePicker/`

Component to comfortably enter a date time value. The `DateTimePicker` component
automatically uses the user's settings for the locale and timezone and formats
the date and time accordingly.

### Import

`tsx
import { DateTimePicker } from '@dynatrace/strato-components/forms';
`

### Demo

```tsx
import { DateTimePicker } from '@dynatrace/strato-components/forms';

const Basic = () => {
  return <DateTimePicker />;
};
```

```tsx
import { DateTimePicker } from '@dynatrace/strato-components/forms';

const Basic = () => {
  return <DateTimePicker />;
};
```


### Control state

You can also handle the state of the `DateTimePicker` component, making it
controlled. In order to do so, you need to set the `value` prop to assign the
state value. In addition, you need to use the `onChange` prop to provide a
handler that is called when the state of the `DateTimePicker` changes.

```tsx
import { useState } from 'react';

import {
  DateTimePicker,
  type DateTimePickerProps,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [isoDate, setIsoDate] = useState<DateTimePickerProps['value']>(() =>
    new Date().toISOString()
  );

  return <DateTimePicker value={isoDate} onChange={setIsoDate} />;
};
```

```tsx
import { useState } from 'react';

import {
  DateTimePicker,
  type DateTimePickerProps,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [isoDate, setIsoDate] = useState<DateTimePickerProps['value']>(() =>
    new Date().toISOString()
  );

  return <DateTimePicker value={isoDate} onChange={setIsoDate} />;
};
```


### Display types and precision

The `DateTimePicker` component can be used to let users select or display a
date, time, or both. For `time` and `datetime` types, the time precision can be
configured.

```tsx
import { DateTimePicker } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const DisplayType = () => {
  return (
    <Flex>
      <DateTimePicker type="date" />
      <DateTimePicker type="time" precision="milliseconds" />
      <DateTimePicker type="datetime" precision="minutes" />
    </Flex>
  );
};
```

```tsx
import { DateTimePicker } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const DisplayType = () => {
  return (
    <Flex>
      <DateTimePicker type="date" />
      <DateTimePicker type="time" precision="milliseconds" />
      <DateTimePicker type="datetime" precision="minutes" />
    </Flex>
  );
};
```


### Min and max values

Minimum and maximum boundaries for date, time, and datetime values can be set
with the `min` and `max` props. You can provide any ISOString or expression to
be used as upper or lower bound.

```tsx
import {
  DateTimePicker,
  FormField,
  FormFieldMessages,
  Label,
} from '@dynatrace/strato-components/forms';

const MinMax = () => {
  return (
    <FormField>
      <Label>DateTimePicker</Label>
      <DateTimePicker min="2025-01-01" max="now" defaultValue="+1d" />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import {
  DateTimePicker,
  FormField,
  FormFieldMessages,
  Label,
} from '@dynatrace/strato-components/forms';

const MinMax = () => {
  return (
    <FormField>
      <Label>DateTimePicker</Label>
      <DateTimePicker min="2025-01-01" max="now" defaultValue="+1d" />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Validation

You can validate the `DateTimePicker` using the `react-hook-form` package, which
handles error messages. For connecting the form with the component for
validation, you need to register the field with custom error messages and use
the `useForm` hook from `react-hook-form`. By using the `controlState` prop, you
can connect the `DateTimePicker`'s error state and message to that of the form.
This shows a hint in case of an error and applies proper styling to the
component.

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import type { TimeValue } from '@dynatrace/strato-components/core';
import {
  DateTimePicker,
  FormField,
  FormFieldMessages,
  Label,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    datetime: TimeValue | string | null;
  }>({
    mode: 'all',
    defaultValues: {
      datetime: new Date().toISOString(),
    },
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Select a date</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="datetime"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'A DateTime is required.',
              },
              validate(value: TimeValue | string | null) {
                const newValue =
                  typeof value === 'string' ? value : value?.absoluteDate;
                return (
                  (newValue &&
                    new Date(newValue).getTime() < new Date().getTime()) ||
                  'Please choose a date before today.'
                );
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>DateTime</Label>
                <DateTimePicker {...field} max="now" />
                <FormFieldMessages>
                  {error && (
                    <FormFieldMessages.Item
                      variant="error"
                      message={error.message}
                    />
                  )}
                </FormFieldMessages>
              </FormField>
            )}
          />

          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import type { TimeValue } from '@dynatrace/strato-components/core';
import {
  DateTimePicker,
  FormField,
  FormFieldMessages,
  Label,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    datetime: TimeValue | string | null;
  }>({
    mode: 'all',
    defaultValues: {
      datetime: new Date().toISOString(),
    },
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Select a date</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="datetime"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'A DateTime is required.',
              },
              validate(value: TimeValue | string | null) {
                const newValue =
                  typeof value === 'string' ? value : value?.absoluteDate;
                return (
                  (newValue &&
                    new Date(newValue).getTime() < new Date().getTime()) ||
                  'Please choose a date before today.'
                );
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>DateTime</Label>
                <DateTimePicker {...field} max="now" />
                <FormFieldMessages>
                  {error && (
                    <FormFieldMessages.Item
                      variant="error"
                      message={error.message}
                    />
                  )}
                </FormFieldMessages>
              </FormField>
            )}
          />

          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


#### OnChange

The `onChange` callback returns a `TimeValue` when valid and an empty string
when invalid, or null when empty. This information can be helpful to validate
the `DateTimePicker`. The returned ISOStrings are formatted in UTC time, with
`precision` prop defining their precision.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Display types and precision
- Min and max values
- Validation
- OnChange

### Props

Component to comfortably enter a date time value. The `DateTimePicker` component
automatically uses the user's settings for the locale and timezone and formats
the date and time accordingly.

#### DateTimePickerProps

##### Signature:
`export declare type DateTimeerProps = > & & & & DateTimeerTypeProps & & {
 /**
 * Earliest allowed ISOString and timestamp for validation.
 */
 min?: ;
 /**
 * Latest allowed ISOString for validation.
 */
 max?: ;
 /**
 * The placeholder that's shown in the input field if the content is empty.
 */
 placeholder?: ;
};`Still have questions?Find answers in the Dynatrace Community

---

## FieldSet

`/design/components/forms/FieldSet/`

Use `FieldSet` to semantically group related form fields.

OverviewProperties

### Import

`tsx
import { FieldSet } from '@dynatrace/strato-components/forms';
`

### Use cases

#### Use multiple fieldsets

It is possible to nest several components inside each other. To do
so, you can simply put it inside any other `Fieldset` component.

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import { FieldSet, Switch } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';

const MultipleFieldSets = () => {
  const [value, setValue] = useState<Timeframe | null>(null);
  const [resolveData, setResolveData] = useState(false);
  const [tracing, setTracing] = useState(false);

  return (
    <FieldSet name="general-parameters">
      <FieldSet.Legend>General parameters</FieldSet.Legend>
      <FieldSet name="timeframe">
        <FieldSet.Legend>Timeframe</FieldSet.Legend>
        <Flex>
          <TimeframeSelector value={value} onChange={setValue} />
        </Flex>
        <Text>
          General timeframe to use if no specific timeframe is used in a query
        </Text>
      </FieldSet>
      <FieldSet>
        <FieldSet.Legend>Resolve data</FieldSet.Legend>
        <Switch value={resolveData} onChange={setResolveData}>
          Enable resolving of dimensional queries
        </Switch>
      </FieldSet>
      <FieldSet>
        <FieldSet.Legend>Tracing</FieldSet.Legend>
        <Switch value={tracing} onChange={setTracing}>
          Activate additional tracing outputs
        </Switch>
      </FieldSet>
    </FieldSet>
  );
};
```

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import { FieldSet, Switch } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';

const MultipleFieldSets = () => {
  const [value, setValue] = useState<Timeframe | null>(null);
  const [resolveData, setResolveData] = useState(false);
  const [tracing, setTracing] = useState(false);

  return (
    <FieldSet name="general-parameters">
      <FieldSet.Legend>General parameters</FieldSet.Legend>
      <FieldSet name="timeframe">
        <FieldSet.Legend>Timeframe</FieldSet.Legend>
        <Flex>
          <TimeframeSelector value={value} onChange={setValue} />
        </Flex>
        <Text>
          General timeframe to use if no specific timeframe is used in a query
        </Text>
      </FieldSet>
      <FieldSet>
        <FieldSet.Legend>Resolve data</FieldSet.Legend>
        <Switch value={resolveData} onChange={setResolveData}>
          Enable resolving of dimensional queries
        </Switch>
      </FieldSet>
      <FieldSet>
        <FieldSet.Legend>Tracing</FieldSet.Legend>
        <Switch value={tracing} onChange={setTracing}>
          Activate additional tracing outputs
        </Switch>
      </FieldSet>
    </FieldSet>
  );
};
```


#### Disable a fieldset

To disable a `FieldSet` and all controls grouped by it, you can simply add the
`disabled` prop.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Use multiple fieldsets
- Disable a fieldset

### Props

#### FieldSetProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `disabled?` | | `false` | Whether the fieldset and all its fields are disabled or not.
 | `name?` | | | The name associated with the group in a form.

## FieldSet.Legend

Use `FieldSet` to semantically group related form fields.

OverviewProperties

#### FieldSetLegendProps
extends`, , , `Still have questions?Find answers in the Dynatrace Community

---

## FormField

`/design/components/forms/FormField/`

The `FormField` component is the outermost layout component of an input
component (for example `TextInput`), providing support for displaying a sibling
`label` element alongside.

It also features responsive design: small containers show the label elements
aligned on top of the input. In comparison, wider containers show input elements
with their label aligned to the left.

The form field is child-agnostic.

OverviewProperties

### Import

`tsx
import { FormField } from '@dynatrace/strato-components/forms';
`

### Use cases

You can use the `FormField` component to render any form control. You also need
to render a label for accessibility. The `FormField` can only render one form
control component inside its children, as shown in the example below.

#### Set a label

The connection between the form control inside the `FormField` component and the
label is done automatically if you don't set any `id` on the control. However,
if you do set a custom `id`, you need to handle the connection manually by
adding the `htmlFor` prop to the `Label` with the same `id`, as shown below.
Furthermore, the `required`, `disabled`, and `id` props are stored in a shared
context, so they're also passed to the corresponding input.

#### Show form field messages and custom hints and errors

You can use the `FormFieldMessages` component to render messages (errors and
hints) coming from the form control element. If no render function is provided,
all messages are displayed, but you can also use a function to filter the
messages. You can add custom hint or error messages to the `FormFieldMessages`,
which will automatically be connected to the form control. If an error is
provided, the form submission is disabled for the connected form control.

#### Use a custom layout

You can customize the layout to show the label in different positions relative
to the `FormField`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Set a label
- Show form field messages and custom hints and errors
- Use a custom layout

### Props

The `FormField` component is the outermost layout component of an input
component (for example `TextInput`), providing support for displaying a sibling
`label` element alongside.

It also features responsive design: small containers show the label elements
aligned on top of the input. In comparison, wider containers show input elements
with their label aligned to the left.

The form field is child-agnostic.

OverviewProperties

#### FormFieldProps
extends`, , , , , , , `

#### SharedFormFieldProps
 |
 | Name | Type | Default | Description
 | `controlId?` | | | An id for the form control (also needed to link the label).
 | `required?` | | `false` | Defines if any form control within the FormField is required.
 | `disabled?` | | `false` | Defines if any form control within the FormField is disabled.
 | `ariaDisabled?` | | | Defines if any form control within the FormField is aria-disabled.
 | `readOnly?` | | `false` | Defines if any form control within the FormField is read-only.

#### FormFieldMessages, FormFieldMessages.Item

You can use the `FormFieldMessages.Item` component to render any custom message
item inside the `FormFieldMessages`. Similarly, you can use the
`ShowFormFieldMessages.Item` component to render any message item coming from
the form control.

#### FormFieldMessageItemProps

##### Signature:
`export declare type FormFieldMessageItemProps = & {
 /**
 * Content of the FormFieldMessage
 */
 message?: ;
 /**
 * The validity state key set on the form control element.
 * The automatically supported errors depend on the keys from the browser API (See https://developer.mozilla.org/en-US/docs/Web/API/ValidityState).
 * In case the same key is used for additional validation, the message will be overwritten by the default.
 *
 */
 validityStateKey?: ;
};`Still have questions?Find answers in the Dynatrace Community
- FormFieldMessages, FormFieldMessages.Item

---

## Label

`/design/components/forms/Label/`

The `Label` component allows users to add an associated text to another form
control by using the `FormField` component.

OverviewProperties

### Import

`tsx
import { Label } from '@dynatrace/strato-components/forms';
`

### Use cases

#### Variants

You can use the `required` prop to mark the label as required. This will then
show an asterisk next to it as an indicator to the user that the connected field
is required. You can also disable the label using the `disabled` prop.

#### Complex label

When using a more complex custom label (not string-based), it is necessary to
handle the visualization of the required property in the custom label itself. In
the basic implementation, it adds an asterisk in the `:after` of the label.

`tsx
&:after { content: ' *';}
`

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Variants
- Complex label

### Props

The `Label` component allows users to add an associated text to another form
control by using the `FormField` component.

OverviewProperties

#### LabelProps
extends`, , , , , , ` |
 | Name | Type | Default | Description
 | `htmlFor?` | | | Defines the id of a labelable form related field.
 | `required?` | | `false` | If there is a wrapping form field then this label uses the required value
from the form field, otherwise it uses this required value. The label
has a visual style to indicate the associated field is a mandatory field.
 | `disabled?` | | `false` | If there is a wrapping form field then this label uses the disabled value
from the form field, otherwise it uses this disabled value. The label
has a visual style to indicate the associated field is disabled.Still have questions?Find answers in the Dynatrace Community

---

## NumberInput

`/design/components/forms/NumberInput/`

DeprecatedThis component is deprecated and will be removed in a future release. Please use
the NumberInputV2 component instead.
Number inputs let users enter and edit integers and floating-point numbers.

OverviewProperties

### Import

`tsx
import { NumberInput } from '@dynatrace/strato-components/forms';
`

### Use cases

This is the simplest version of the `NumberInput`, which is uncontrolled and
therefore handles its state internally. You can also set a specific initial
value using the `defaultValue` prop.

#### Control the state

The `NumberInput` can also be controlled, meaning that you can handle the state.
To do so, you need to use the `onChange` prop to provide a handler that is
called when a valid number can be received. Which is when the input gets
blurred or a step button is clicked - it does not happen on typing. You also
need to assign the value from the state to the `NumberInput` by setting the
`value` prop.

#### Validate

This example shows how you can validate the `NumberInput` using the
`react-hook-form` package, which handles error messages. For connecting the form
with the `NumberInput` and validating, you need to register the field with
custom error messages and use the `useForm` hook from `react-hook-form`. Also,
by using the `controlState` prop, you can override the error messages and
connect the input's error state and message to that of the form. This shows a
hint in case of an error and applies proper styling to the component.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Control the state
- Validate

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  NumberInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    size: number | null;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Settings</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="size"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'The number of clusters is required',
              },
              min: {
                value: 10,
                message: 'We do not support values lower than 10',
              },
              max: {
                value: 150,
                message: 'We do not support value greater than 150',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Number of clusters</Label>
                <NumberInput
                  placeholder="eg. 50"
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message || 'We support values from 10 to 150',
                  }}
                  {...field}
                />
              </FormField>
            )}
          />

          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  NumberInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    size: number | null;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Settings</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="size"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'The number of clusters is required',
              },
              min: {
                value: 10,
                message: 'We do not support values lower than 10',
              },
              max: {
                value: 150,
                message: 'We do not support value greater than 150',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Number of clusters</Label>
                <NumberInput
                  placeholder="eg. 50"
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message || 'We support values from 10 to 150',
                  }}
                  {...field}
                />
              </FormField>
            )}
          />

          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Props

DeprecatedThis component is deprecated and will be removed in a future release. Please use
the NumberInputV2 component instead.
Number inputs let users enter and edit integers and floating-point numbers.

OverviewProperties

#### NumberInputProps

##### Signature:
`export declare type NumberInputProps = & > & & & {
 /** Handler that is called when a key is pressed. */
 onKeyDown?: <>;
 /** Minimum amount of the input. */
 min?: | ;
 /** Maximum amount of the input. */
 max?: | ;
 /** Defines the step size in which increments/decrements can be performed on the input. */
 step?: ;
};`Still have questions?Find answers in the Dynatrace Community

---

## NumberInputV2

`/design/components/forms/NumberInputV2/`

Use `NumberInputV2` to let users enter integers and floating-point numbers.

Migration

### Import

`tsx
import { NumberInputV2 } from '@dynatrace/strato-components/forms';
`

### Demo

This is the simplest version of the `NumberInputV2`, which is uncontrolled and
therefore handles its state internally. You can also set a specific initial
value using the `defaultValue` prop.

### Control state

The `NumberInput` can also be controlled, meaning that you can handle the state.
To do so, you need to use the `onChange` prop to provide a handler that is
called when a valid number can be received. Which is when the input gets
blurred or a step button is clicked - it does not happen on typing. You also
need to assign the value from the state to the `NumberInput` by setting the
`value` prop.

### Validate with min and max

The `NumberInput` has built-in support for the `min` and `max` props. When the
entered value falls outside the allowed range, the component automatically
displays a validation error. Add `FormFieldMessages` inside `FormField` to
render those messages.

### Validate with step

The `step` prop constrains the accepted values to specific increments. If the
entered value does not align with the step (relative to `min` if provided), a
validation error is shown automatically.

The value can be incremented or decremented in the following ways:

 |
 | Interaction | Behaviour
 | `↑` / `↓` arrow keys | Increment / decrement by one step
 | Scroll wheel (when focused) | Same as arrow keys
 | `Home` key | Jumps to `min` — only when `min` is set
 | `End` key | Jumps to `max` — only when `max` is set
Snap-to-step alignment: if the current value is not aligned with the step
when an arrow key or scroll event fires, the first interaction snaps the value
to the nearest step boundary instead of moving a full step — subsequent
interactions then move by exactly one step as expected.

Clamping: stepping always respects `min` and `max`. The value will not go
below `min` or above `max`. When `max` and `step` are both set, the highest
reachable step-aligned value may be less than `max` if `max` is not itself
step-aligned.

Read-only inputs: all step interactions are suppressed when the input is in
`readOnly` mode.

### Step multiplier

The `stepMultiplier` prop scales how far the value jumps when using the arrow
keys or the scroll wheel. The total change per interaction is
`step × stepMultiplier` (or just `stepMultiplier` when no `step` is set). The
`Home` and `End` keys are not affected by `stepMultiplier` — they always jump
directly to `min` or `max`. This is useful when users need both fine-grained
control and the ability to make large adjustments quickly — for example,
allocating memory where small tweaks matter but jumping by 10 at a time is also
common. Note: `stepMultiplier` must be an integer. If a floating‑point value
is provided, it is automatically truncated to its integer part before being
applied.

### Number formats and localization

The `NumberInput` uses the user's regional format (from
`@dynatrace-sdk/user-preferences`) to interpret and display numbers. Because of
this it accepts a wide range of input formats.

#### Valid number formats

A value is fully valid once it is parseable as a JavaScript number. The
following formats are accepted:

 |
 | Format | Example
 | Plain integer | `42`, `-7`, `+100`
 | Decimal | `3.14` or `3,14` (locale-dependent decimal separator)
 | Scientific notation | `1.5e3`, `-2.4E-6`, `1e+10`
 | Locale-grouped | `1,234,567` (EN) / `1.234.567` (DE) / `1 234 567` (FR) / `1'234'567` (CH)
The input accepts `.` and `,` interchangeably as a decimal separator — the
correct interpretation is inferred automatically from grouping context (e.g.
`1,234` is treated as a grouped thousand, while `1,5` is treated as a decimal
value of 1.5).

#### Typing behaviour

While the user is typing, the field is intentionally permissive: intermediate
states such as `-`, `1.`, or `1.5e` are kept in the input without being
rejected. The `onChange` callback is only fired when a fully valid number
can be parsed. Clearing the field fires `onChange` with `null`.

#### Paste behaviour

When a formatted number is pasted (e.g. `1,234,567.89` copied from a spreadsheet
or `1.234.567,89` from a German locale), the component attempts to normalise it
automatically. It strips locale-specific grouping separators (spaces,
apostrophes `'`, commas, or dots used as thousands separators) and converts the
remaining decimal separator to the value expected by the current locale. If the
pasted string cannot be resolved to a valid number it is discarded and the
previous value is restored.Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Validate with min and max
- Validate with step
- Step multiplier
- Number formats and localization
- Valid number formats
- Typing behaviour
- Paste behaviour

### Props

Use `NumberInputV2` to let users enter integers and floating-point numbers.

Migration

#### NumberInputV2Props

##### Signature:
`export declare type NumberInputV2Props = & > & & & & {
 /** Minimum amount of the input.
 * @defaultValue */
 min?: ;
 /** Maximum amount of the input.
 * @defaultValue */
 max?: ;
 /** Defines the step in which increments/decrements can be performed on the input and validates the value.
 * Must be a positive greater than 0. Values that are negative, zero, NaN, or default to 1.
 * @defaultValue */
 step?: ;
 /** Multiplier applied to `step` (or 1 if no `step` is set) to determine how much the value changes
 * when using arrow keys or the scroll wheel. Must be a positive integer greater than 0.
 * Values that are negative, zero, NaN, or default to 1. Decimal values are truncated to the nearest integer.
 * @defaultValue 1 */
 stepMultiplier?: ;
};`

#### NumberInput.Prefix, NumberInput.Suffix

You can use the `NumberInput.Prefix` component to render custom content in front
of the input, or the `NumberInput.Suffix` component if you need to render
content after it.

#### BaseInputContentProps
extends |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Prefix slot.

#### NumberInput.Button

You can use the `NumberInput.Button` component to render a button inside the
`NumberInput.Prefix` or `NumberInput.Suffix` component.

#### BaseInputButtonProps
extends`, , , , , ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the BaseInput Button slot, preferably an icon or a similar visual element
 | `disabled?` | | `false` | If a button is disabled e.g. it cannot be interacted with.
By default, it inherits the disabled prop of the BaseInput, but can be overwritten.
 | `tooltipText?` | | | If specified, a tooltip is rendered with this text, which describes what the button does.
Please also consider translating the text in an internationalized context and use a short text description for the tooltip.
The positioning and placing of the according tooltip will be handled by the component.
 | `tooltipBehavioralTrackingProps?` | | | Behavioral tracking props to forward exclusively to the tooltip overlay.
These will not be applied to the button itself.
 | `onClick?` | | | Called when the button is interacted with.
 | `readOnly?` | | | Determines whether the input is in read-only mode.Still have questions?Find answers in the Dynatrace Community
- NumberInput.Prefix, NumberInput.Suffix
- NumberInput.Button

---

## PasswordInput

`/design/components/forms/PasswordInput/`

The `PasswordInput` component can be used to hide user input. Always use a
`PasswordInput` when your app asks for sensitive data, such as a password. Users
can click on the eye icon to hide or show their data.

### Import

`tsx
import { PasswordInput } from '@dynatrace/strato-components/forms';
`

### Demo

This is the simplest version of the `PasswordInput`, which is uncontrolled and
therefore handles its state internally. You can also set a specific initial
value using the `defaultValue` prop.

```tsx
import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Password</Label>
      <PasswordInput />
    </FormField>
  );
};
```

```tsx
import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Password</Label>
      <PasswordInput />
    </FormField>
  );
};
```


### Control state

The `PasswordInput` can also be controlled, meaning that you can handle the
state. To do so, you need to use the `onChange` prop to provide a handler that
is called when the internal state of the input changes. You also need to assign
the value from the state to the `PasswordInput` by setting the `value` prop.

```tsx
import { useState } from 'react';

import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Password</Label>
      <PasswordInput value={value} onChange={setValue} />
    </FormField>
  );
};
```

```tsx
import { useState } from 'react';

import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Password</Label>
      <PasswordInput value={value} onChange={setValue} />
    </FormField>
  );
};
```


### Customize tooltip text

You can use the `PasswordInput.Tooltip` to customize the text displayed if the
password input text is either shown or hidden.

```tsx
import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';

const CustomTooltip = () => {
  return (
    <FormField>
      <Label>Password</Label>
      <PasswordInput>
        <PasswordInput.Tooltip
          showText="Show the password text"
          hideText="Hide the password text"
        />
      </PasswordInput>
    </FormField>
  );
};
```

```tsx
import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';

const CustomTooltip = () => {
  return (
    <FormField>
      <Label>Password</Label>
      <PasswordInput>
        <PasswordInput.Tooltip
          showText="Show the password text"
          hideText="Hide the password text"
        />
      </PasswordInput>
    </FormField>
  );
};
```


### Validation

This example shows how you can validate the `PasswordInput` using the
`react-hook-form` package, which handles error messages. For connecting the form
with the `PasswordInput` and validating, you need to register the field with
custom error messages and use the `useForm` hook from `react-hook-form`. Also,
by using the `controlState` prop, you can override the error messages and
connect the input's error state and message to that of the form. This shows a
hint in case of an error and applies proper styling to the component. You can
also use the `pattern` prop to provide a RegEx that defines which characters are
allowed.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Customize tooltip text
- Validation

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    formState: { isSubmitSuccessful },
    control,
    reset,
  } = useForm<{
    password: string | undefined;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Settings</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="password"
            control={control}
            rules={{
              validate: (value) => {
                return (
                  (value && value.length >= 8) ||
                  'Password has to have at least 8 characters.'
                );
              },
              pattern: {
                value: /(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+/,
                message: 'Passphrases must contain numbers and characters',
              },
              required: {
                value: true,
                message: 'Please enter a password.',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Number of clusters</Label>
                <PasswordInput
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                />
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  PasswordInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    formState: { isSubmitSuccessful },
    control,
    reset,
  } = useForm<{
    password: string | undefined;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Settings</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="password"
            control={control}
            rules={{
              validate: (value) => {
                return (
                  (value && value.length >= 8) ||
                  'Password has to have at least 8 characters.'
                );
              },
              pattern: {
                value: /(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+/,
                message: 'Passphrases must contain numbers and characters',
              },
              required: {
                value: true,
                message: 'Please enter a password.',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Number of clusters</Label>
                <PasswordInput
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                />
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Props

The `PasswordInput` component can be used to hide user input. Always use a
`PasswordInput` when your app asks for sensitive data, such as a password. Users
can click on the eye icon to hide or show their data.

#### PasswordInputProps

##### Signature:
`export declare type PasswordInputProps = & ) => > & & ;`

### PasswordInput.Tooltip

#### PasswordInputTooltipProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `children?` | | | Elements to be displayed in the PasswordInput tooltip slot, preferably an icon or a similar visual element
 | `showText?` | | | If specified, the tooltip is rendered with this text when the password is shown, which describes what the trigger does.
Please also consider translating the text in an internationalized context and use a short text description for the tooltip.
 | `hideText?` | | | If specified, the tooltip is rendered with this text when the password is hidden, which describes what the trigger does.
Please also consider translating the text in an internationalized context and use a short text description for the tooltip.Still have questions?Find answers in the Dynatrace Community
- PasswordInput.Tooltip

---

## Radio

`/design/components/forms/Radio/`

Radio buttons allow users to select one option from a group of related options.
To group options, wrap the `Radio` components inside a `RadioGroup` component.
If you want to give the user more than 4 options, consider using a `Select`
component.

### Import

`tsx
import { Radio } from '@dynatrace/strato-components/forms';
`

### Use cases

This is the simplest version of the `Radio`, which is uncontrolled and therefore
handles its state internally. You can also set a specific initial value using
the `defaultValue` prop.

Note: You need to add the `name` prop to link the radio buttons correctly.

#### Control the state

The `Radio` can also be controlled, meaning that you can handle the state. To do
so, you need to use the `onChange` prop to provide a handler that is called when
the internal state of the `Radio` changes. You also need to assign the value
from the state to the `Radio` by setting the `value` prop.

#### Validate

This example shows how you can validate the `Radio` using the `react-hook-form`
package, which handles error messages. For connecting the form with the `Radio`
and validating, you need to register the field with custom error messages and
use the `useForm` hook from `react-hook-form`. Also, by using the `controlState`
prop, you can override the error messages and connect the `Radio`'s error state
and message to that of the form. This shows a hint in case of an error and
applies proper styling to the component.

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  Radio,
  RadioGroup,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{ radio: string }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Settings</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="radio"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Please select an option',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Scale</Label>
                <RadioGroup
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                >
                  <Radio value="logarithmic">logarithmic</Radio>
                  <Radio value="linear">linear</Radio>
                </RadioGroup>
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  Radio,
  RadioGroup,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{ radio: string }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Settings</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="radio"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Please select an option',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Scale</Label>
                <RadioGroup
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                >
                  <Radio value="logarithmic">logarithmic</Radio>
                  <Radio value="linear">linear</Radio>
                </RadioGroup>
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


#### Disable

You can disable the entire `RadioGroup` by adding the `disabled` prop to it.
Alternatively, you can also disable individual items by adding the `disabled`
prop to the `Radio` item.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Control the state
- Validate
- Disable

```tsx
import {
  FieldSet,
  Radio,
  RadioGroup,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Disabled = () => {
  return (
    <Flex gap={8}>
      <FieldSet>
        <FieldSet.Legend>Disabled RadioGroup</FieldSet.Legend>
        <RadioGroup disabled name="radio-disabled">
          <Radio aria-label="hosts" value="hosts">
            Hosts
          </Radio>
          <Radio aria-label="services" value="services">
            Services
          </Radio>
          <Radio aria-label="processGroups" value="processGroups">
            Process Groups
          </Radio>
        </RadioGroup>
      </FieldSet>
      <FieldSet>
        <FieldSet.Legend>Disabled Radio</FieldSet.Legend>
        <RadioGroup name="fieldset-disabled">
          <Radio aria-label="hosts" value="hosts" disabled>
            Hosts
          </Radio>
          <Radio aria-label="services" value="services">
            Services
          </Radio>
          <Radio aria-label="processGroups" value="processGroups">
            Process Groups
          </Radio>
        </RadioGroup>
      </FieldSet>
    </Flex>
  );
};
```

```tsx
import {
  FieldSet,
  Radio,
  RadioGroup,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Disabled = () => {
  return (
    <Flex gap={8}>
      <FieldSet>
        <FieldSet.Legend>Disabled RadioGroup</FieldSet.Legend>
        <RadioGroup disabled name="radio-disabled">
          <Radio aria-label="hosts" value="hosts">
            Hosts
          </Radio>
          <Radio aria-label="services" value="services">
            Services
          </Radio>
          <Radio aria-label="processGroups" value="processGroups">
            Process Groups
          </Radio>
        </RadioGroup>
      </FieldSet>
      <FieldSet>
        <FieldSet.Legend>Disabled Radio</FieldSet.Legend>
        <RadioGroup name="fieldset-disabled">
          <Radio aria-label="hosts" value="hosts" disabled>
            Hosts
          </Radio>
          <Radio aria-label="services" value="services">
            Services
          </Radio>
          <Radio aria-label="processGroups" value="processGroups">
            Process Groups
          </Radio>
        </RadioGroup>
      </FieldSet>
    </Flex>
  );
};
```


### Props

Radio buttons allow users to select one option from a group of related options.
To group options, wrap the `Radio` components inside a `RadioGroup` component.
If you want to give the user more than 4 options, consider using a `Select`
component.

#### RadioProps

##### Signature:
`export declare type RadioProps = , | > & & & & & & & ;`

#### RadioGroupProps

##### Signature:
`export declare type RadioGroupProps = ) => | > & & & & ;`Still have questions?Find answers in the Dynatrace Community

---

## SearchInput

`/design/components/forms/SearchInput/`

Use the `SearchInput` component for search queries. It includes a built-in
`Clear` button for quick resets.

### Import

`tsx
import { SearchInput } from '@dynatrace/strato-components/forms';
`

### Demo

This is the simplest version of the `SearchInput`, which is uncontrolled and
therefore handles its state internally. You can also set a specific initial
value using the `defaultValue` prop. The `SearchInput` provides unified search
styling and a built-in `Clear` button.

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Search</Label>
      <SearchInput />
    </FormField>
  );
};
```

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Search</Label>
      <SearchInput />
    </FormField>
  );
};
```


### Control state

The `SearchInput` can also be controlled, meaning that you can handle the state.
To do so, use the `onChange` prop to provide a handler that is called when the
internal state of the `SearchInput` changes. You also need to assign the value
from the state to the `SearchInput` by setting the `value` prop.

```tsx
import { useState } from 'react';

import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Search</Label>
      <SearchInput value={value} onChange={setValue} />
    </FormField>
  );
};
```

```tsx
import { useState } from 'react';

import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Search</Label>
      <SearchInput value={value} onChange={setValue} />
    </FormField>
  );
};
```


### Add a suffix

The component also supports a `SearchInput.Suffix`. The suffix serves as a
container at the end for an icon, some text, or a `SearchInput.Button` with a
click handler. A divider is shown if there is both a suffix and a `Clear`
button. In case of a large suffix area you might want to adjust the CSS
min-width to avoid flickering with the conditionally shown clear button.

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';
import { HelpIcon } from '@dynatrace/strato-icons';

const Suffix = () => {
  return (
    <Flex gap={8}>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search">
          <SearchInput.Suffix>
            <HelpIcon />
          </SearchInput.Suffix>
        </SearchInput>
      </FormField>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search">
          <SearchInput.Suffix>
            <Text>@dynatrace.com</Text>
            <SearchInput.Button>
              <HelpIcon />
            </SearchInput.Button>
          </SearchInput.Suffix>
        </SearchInput>
      </FormField>
    </Flex>
  );
};
```

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';
import { HelpIcon } from '@dynatrace/strato-icons';

const Suffix = () => {
  return (
    <Flex gap={8}>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search">
          <SearchInput.Suffix>
            <HelpIcon />
          </SearchInput.Suffix>
        </SearchInput>
      </FormField>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search">
          <SearchInput.Suffix>
            <Text>@dynatrace.com</Text>
            <SearchInput.Button>
              <HelpIcon />
            </SearchInput.Button>
          </SearchInput.Suffix>
        </SearchInput>
      </FormField>
    </Flex>
  );
};
```


### Variants

The `SearchInput` can be styled differently using the `variant` prop. The
default visual representation is `default`, but can also be set to `minimal`.

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex gap={8}>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search" />
      </FormField>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search" variant="minimal" />
      </FormField>
    </Flex>
  );
};
```

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex gap={8}>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search" />
      </FormField>
      <FormField>
        <Label>Search</Label>
        <SearchInput placeholder="Type to search" variant="minimal" />
      </FormField>
    </Flex>
  );
};
```


### Make the input read-only

The `SearchInput` can be set to read-only by simply adding the `readOnly` prop.

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';

const ReadOnly = () => {
  return (
    <FormField>
      <Label>Search</Label>
      <SearchInput readOnly />
    </FormField>
  );
};
```

```tsx
import {
  FormField,
  Label,
  SearchInput,
} from '@dynatrace/strato-components/forms';

const ReadOnly = () => {
  return (
    <FormField>
      <Label>Search</Label>
      <SearchInput readOnly />
    </FormField>
  );
};
```


### Validate

The `SearchInput` supports an error state, which can be triggered in two primary
ways:

- Form submission: If the form containing the `SearchInput` is submitted
with invalid or missing data, the component can reflect the error state.

- Validation function: Validation logic can be applied to determine whether
the selected value meets the required criteria.

This example demonstrates how to show users a validation message using
`FormFieldMessages`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Add a suffix
- Variants
- Make the input read-only
- Validate

```tsx
import { useRef, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  SearchInput,
  FormFieldMessages,
  type FormControlRef,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Validation = () => {
  const searchInputRef = useRef<FormControlRef<HTMLDivElement> | null>(null);
  const [showCustomError, setShowCustomError] = useState(false);

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
      }}
    >
      <Flex flexDirection="column" gap={16}>
        <FormField>
          <Label>Search</Label>
          <SearchInput ref={searchInputRef} required />
          <FormFieldMessages>
            {(messages) => {
              if (showCustomError) {
                return (
                  <FormFieldMessages.Item variant="error">
                    Custom error for the search input
                  </FormFieldMessages.Item>
                );
              }
              if (!messages || messages.length === 0) {
                return (
                  <FormFieldMessages.Item variant="hint">
                    Hint for the search input
                  </FormFieldMessages.Item>
                );
              }

              return messages.map((msg) => (
                <FormFieldMessages.Item key={msg.id} {...msg} />
              ));
            }}
          </FormFieldMessages>
        </FormField>

        <Flex gap={12}>
          <Button variant="accent" type="submit">
            Submit
          </Button>
          <Button
            variant="emphasized"
            onClick={() => setShowCustomError(!showCustomError)}
          >
            Toggle custom error
          </Button>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { useRef, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  SearchInput,
  FormFieldMessages,
  type FormControlRef,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Validation = () => {
  const searchInputRef = useRef<FormControlRef<HTMLDivElement> | null>(null);
  const [showCustomError, setShowCustomError] = useState(false);

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
      }}
    >
      <Flex flexDirection="column" gap={16}>
        <FormField>
          <Label>Search</Label>
          <SearchInput ref={searchInputRef} required />
          <FormFieldMessages>
            {(messages) => {
              if (showCustomError) {
                return (
                  <FormFieldMessages.Item variant="error">
                    Custom error for the search input
                  </FormFieldMessages.Item>
                );
              }
              if (!messages || messages.length === 0) {
                return (
                  <FormFieldMessages.Item variant="hint">
                    Hint for the search input
                  </FormFieldMessages.Item>
                );
              }

              return messages.map((msg) => (
                <FormFieldMessages.Item key={msg.id} {...msg} />
              ));
            }}
          </FormFieldMessages>
        </FormField>

        <Flex gap={12}>
          <Button variant="accent" type="submit">
            Submit
          </Button>
          <Button
            variant="emphasized"
            onClick={() => setShowCustomError(!showCustomError)}
          >
            Toggle custom error
          </Button>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Props

Use the `SearchInput` component for search queries. It includes a built-in
`Clear` button for quick resets.

#### SearchInputProps

##### Signature:
`export declare type SearchInputProps = & & & & & & > & ;`

#### SearchInput.Suffix

Use the `SearchInput.Suffix` component to render content after the input.

Prop Table did not receive data

#### SearchInput.Button

Use the `SearchInput.Button` component to render a button inside the
`SearchInput.Suffix` component.

Prop Table did not receive dataStill have questions?Find answers in the Dynatrace Community
- SearchInput.Suffix
- SearchInput.Button

---

## Select

`/design/components/forms/Select/`

The `Select` component allows you to choose one or multiple options from a
collapsed dropdown with options.

### Import

`tsx
import { Select } from '@dynatrace/strato-components/forms';
`

### Demo

```tsx
import {
  SegmentSelector,
  useSegments,
} from '@dynatrace/strato-components/filters';

const Basic = () => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { segments } = useSegments();

  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector />
    </div>
  );
};
```

```tsx
import {
  SegmentSelector,
  useSegments,
} from '@dynatrace/strato-components/filters';

const Basic = () => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { segments } = useSegments();

  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector />
    </div>
  );
};
```


### Use multiple selection

The `Select` supports multiple selection. You can enable that by adding the
`multiple` prop. If enabled, the "Select all" option gets added automatically.

### Group options together

You can use the `Select.Groups` to group more options in the same group.

### Control state

The `Select` can also be controlled, meaning that you can handle the selection
state. To do so, you need to use the `onChange` prop to provide a handler that
is called when the internal state changes. That state can be modified and is
applied as soon as it's passed to the `value` prop.

### Show custom placeholder

You can use the `Select.Trigger` component to show a placeholder for the trigger
button by adding the `placeholder` prop. If no option is selected, the
`placeholder` value is shown by default. Notice that the `clearable` prop is
used here to enable empty selection.

### Show custom display value

You can use the `Select.DisplayValue` component to customize what is rendered on
the trigger. By default, the placeholder is shown when no option is selected.
You can also render content inside a `Select.Prefix` component to show an icon
in front of the trigger display value for example. When you select a value, the
content inside the `Select.DisplayValue` slot is then rendered inside the
trigger.

### Customize trigger

You can use the `Select.CustomTrigger` component to render custom content inside
the trigger slot, so you can control the styling or its rendered text.

NoteAs the `Select` component renders a hidden input inside the trigger for forms
integration, if you're using an interactive element (e.g. a `
Disable options
In the Select`, you can disable each option separately by adding the `disabled`
prop on the `Select.Option` component. Otherwise, if you need to disable the
whole `Select` component, you can add the `disabled` prop directly.

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import { SegmentSelector } from '@dynatrace/strato-components/filters';
import { ChevronDownSmallIcon, ContainerIcon } from '@dynatrace/strato-icons';

const CustomTrigger = () => {
  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector>
        <SegmentSelector.CustomTrigger>
          {({ displayValue, isLoading }, props) => (
            <Button {...props} loading={isLoading}>
              <Button.Prefix>
                <ContainerIcon />
              </Button.Prefix>
              {displayValue}
              <Button.Suffix>
                <ChevronDownSmallIcon />
              </Button.Suffix>
            </Button>
          )}
        </SegmentSelector.CustomTrigger>
      </SegmentSelector>
    </div>
  );
};
```

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import { SegmentSelector } from '@dynatrace/strato-components/filters';
import { ChevronDownSmallIcon, ContainerIcon } from '@dynatrace/strato-icons';

const CustomTrigger = () => {
  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector>
        <SegmentSelector.CustomTrigger>
          {({ displayValue, isLoading }, props) => (
            <Button {...props} loading={isLoading}>
              <Button.Prefix>
                <ContainerIcon />
              </Button.Prefix>
              {displayValue}
              <Button.Suffix>
                <ChevronDownSmallIcon />
              </Button.Suffix>
            </Button>
          )}
        </SegmentSelector.CustomTrigger>
      </SegmentSelector>
    </div>
  );
};
```


### Make selection clearable

In a single select, the `clearable` prop adds a button to the overlay when an
option is selected to allow users to deselect the option. By default,
`clearable` is set to `false` for the single select and `true` if multiple
selection is enabled. For the multi-select, an option is added to select or
deselect all options.

### Filter options

You can search through options by adding the `Select.Filter` component. This
renders a search input, where you can type the filtering term and filter the
options on the client-side. If no options are found after filtering, you can
also customize the shown message by adding content to the `Select.EmptyState`
component, which is only valid within the `Select.Content` element. Otherwise,
the default message is shown: "No items found.".

### Control filtering of options

You can also control the filtering of the options by adding the `value` and the
`onFilterChange` props on the `Select.Filter` component.

### Use complex objects as values

There are some known limitations when using complex objects as option values.
For the `Select` to be able to keep the user's selection between renders, you
can opt for one of the following approaches:

- Use the controlled variant of the `Select`.

- Use cached values inside of your component function (for example, by using
`useMemo` or `useState`).

- Declare variables outside of your component function.

The value returned by a form when the user selects an option depends on the
properties of the selected option.

- If you provide a `textValue`, that will be the returned value.

- If you don't provide a `textValue`, and the `value` can be converted to a
string, the stringified `value` will be returned.

- If you don't provide a `textValue` or a stringifiable `value`, the option
label will be submitted.

- If no `textValue` is given, and neither the `value` nor the option label can
be stringified, a fallback value will be submitted.

### Filter complex options

If you're using a custom component as `Select.Option`, the text value of this
option can't be determined automatically. To enable the filtering of these
options and to show which option is selected, you need to provide a `textValue`
with a string representation of the `Select.Option`.

### Add icons to options

The `Select.SelectOption` component allows adding icons in front of the option
node with the `Select.Prefix` or after it with the `Select.Suffix`. The same can
be done to add prefix and suffix icons inside the `Select.DisplayValue` slot, as
shown above.

### Show loading state

You can show the loading state of the `Select.Option` components by adding the
`loading` prop to the `Select.Content` component.

### Set trigger width

You can set the width of the trigger by adding the `width` prop on the
`Select.Trigger` component and either giving it a fixed value or setting it to
`full`, which would adjust it to the width of its container. By default, it's
set to `content`, so it adjusts to the width of the trigger content.

### Set content width

You can set the width of the content by adding the `width` prop on the
`Select.Content` component and giving it a fixed value. By default, it has a
min-width of 96px and adjusts to the size of the trigger. If the text of the
options is overflowing, the text is truncated at the end by default. However,
you can also add the `TextEllipsis` component directly inside the
`Select.Option` and wrap the text inside it to set the truncation to the start
or middle, if necessary. See
the TextEllipsis documentation for
more details.

### Pass large amounts of data

The `Select` can handle large amounts of options. The select options are
virtualized if the content is too large to fit. The virtualization only affects
the first-level children, so either ungrouped options or groups. Therefore, we
don't recommend having too many options inside a single group to ensure a smooth
user experience.

### Show selected options first

In the `Select`, you can use the `showSelectedOptionsFirst` prop to configure
whether the options should be reordered to show the selected options at the top.
If this is set to `true` the options will be reordered when the overlay is
closed and opened again. For elected options inside an `Select.Group`, this will
position its group at the top, as well as order the option to the top within the
group.

### Validation

This example shows how you can validate the `Select` using the `react-hook-form`
package, which handles error messages. For connecting the form with the `Select`
and validating, you need to register the field with custom error messages and
use the `useForm` hook from `react-hook-form`. Also, by using the `controlState`
prop, you can override the error messages and connect the `Select`'s error state
and message to that of the form. This shows a hint in case of an error and
applies proper styling to the component. You can also add custom validation
logic when registering the `Select` by passing in a `validate` function to the
`register` options.

### React to open state changes

In the `Select` you can react to changes to the open state using the
`onOpenChange` prop. This prop expects a callback method which receives the new
open state as a single `boolean` argument.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Use multiple selection
- Group options together
- Control state
- Show custom placeholder
- Show custom display value
- Customize trigger
- Disable options
- Make selection clearable
- Filter options
- Control filtering of options
- Use complex objects as values
- Filter complex options
- Add icons to options
- Show loading state
- Set trigger width
- Set content width
- Pass large amounts of data
- Show selected options first
- Validation
- React to open state changes

### Props

The `Select` component allows you to choose one or multiple options from a
collapsed dropdown with options.

#### SelectFormsProps

##### Signature:
`export declare type SelectFormsProps = & : <>, (value: ) => > & & & & & ;`

#### SelectBaseProps

##### Signature:
`export declare type SelectBaseProps = );
 /** Name used for the component when submitting it in a form */
 name?: ;
 /** Form name used to connect the component to a form */
 form?: ;
 /**
 * Boolean to determine whether the component is required
 *
 * @defaultValue false
 */
 required?: ;
 /**
 * Whether the component is disabled
 *
 * @defaultValue false
 */
 disabled?: ;
 /**
 * Event handler called when the open state for the select changes
 */
 onOpenChange?: (isOpen: ) => ;
 /**
 * Whether or not the select allows multiple selection or not
 * @defaultValue false
 */
 multiple?: ;
 /**
 * Whether or not the select is clearable.
 * @defaultValue false for single select, true for multi select
 */
 clearable?: ;
 /** Callback that is called when the select trigger loses focus. */
 onBlur?: (e: ) => ;
 /** Callback that is called when the select trigger gets focus. */
 onFocus?: (e: ) => ;
}> & ;`

### Select base components

#### Select.Content

The `Select.Content` wraps all the custom content of the overlay, including the
options, groups, and group labels.

#### SelectContentProps

##### Signature:
`export declare type SelectContentProps = <> & & & & {
 /**
 * The current loading state of the Select.Content. If true, a loading icon is shown.
 * @defaultValue false
 */
 loading?: ;
 /**
 * The width of the Select.Content (overlay). By default it has a min-width of 96px and adjusts to the size of the trigger.
 * @defaultValue
 */
 width?: ;
 /**
 * Whether the selected options are reordered to the top of the options.
 * @defaultValue false
 */
 showSelectedOptionsFirst?: ;
};`

#### Select.Prefix

The `Select.Prefix` component can only be used inside the `Select.DisplayValue`
component or the `Select.Option` component.

#### SelectPrefixProps

##### Signature:
`export declare type SelectPrefixProps = <> & & & ;`

#### Select.Suffix

The `Select.Suffix` component can only be used inside the `Select.DisplayValue`
component or the `Select.Option` component.

#### SelectSuffixProps

##### Signature:
`export declare type SelectSuffixProps = <> & & & ;`

### Select overlay components

#### Select.Option

Every option of the select is represented by the children of the `Select.Option`
component.

#### SelectOptionProps

##### Signature:
`export declare type SelectOptionProps<> = & & & & {
 value: ;
 textValue?: ;
 id?: ;
 ?: ;
 disabled?: ;
};`

#### Select.Group

The `Select.Group` component can be used to add groups to the `Select`
component.

#### SelectGroupProps

##### Signature:
`export declare type SelectGroupProps = <> & & & ;`

#### Select.GroupLabel

When using groups inside the `Select` component, you can name each group by
adding a `Select.GroupLabel` component with a suitable title.

#### SelectGroupLabelProps

##### Signature:
`export declare type SelectGroupLabelProps = <> & & & ;`

#### Select.Filter

#### SelectFilterProps

##### Signature:
`export declare type SelectFilterProps = & & & {
 /**
 * Flag indicating if the client-side filtering should be disabled or not.
 * @defaultValue false
 **/
 disableFiltering?: ;
 /** Defines the default filter . */
 defaultValue?: ;
 /** Defines the filter value. */
 value?: ;
 /** The callback is triggered when the filterValue changes. */
 onChange?: (filterValue: ) => ;
};`

#### Select.EmptyState

#### SelectEmptyStateProps

##### Signature:
`export declare type SelectEmptyStateProps = <> & & & ;`

### Select trigger components

#### Select.Trigger

The `Select.Trigger` component is used to render the trigger that opens or
closes the overlay.

#### SelectTriggerProps

##### Signature:
`export declare type SelectTriggerProps = & & & & {
 /**
 * The placeholder text displayed in the Select.Trigger.
 */
 placeholder?: ;
 /**
 * The width of the Select.Trigger.
 * @defaultValue
 */
 width?: ;
};`

##### Select.DisplayValue

#### SelectDisplayValueProps

##### Signature:
`export declare type SelectDisplayValueProps = <>;`

#### Select.CustomTrigger

#### SelectCustomTriggerProps

##### Signature:
`export declare type SelectCustomTriggerProps = ;`Still have questions?Find answers in the Dynatrace Community
- Select base components
- Select.Content
- Select.Prefix
- Select.Suffix
- Select overlay components
- Select.Option
- Select.Group
- Select.GroupLabel
- Select.Filter
- Select.EmptyState
- Select trigger components
- Select.Trigger
- Select.CustomTrigger

---

## Switch

`/design/components/forms/Switch/`

The `Switch` component allows users to toggle between two different states. You
can set a specific initial value using the `defaultValue` prop for an
uncontrolled switch or setting the initial value of the state of a controlled
switch accordingly. The `name` prop also needs to be specified for identifying
the `Switch` when submitting it in a form.

### Import

`tsx
import { Switch } from '@dynatrace/strato-components/forms';
`

### Use cases

#### Control the state

The `Switch` can also be controlled, meaning that you can handle the state. To
do so, you need to use the `onChange` prop to provide a handler that is called
when the internal state of the `Switch` changes. You also need to assign the
value from the state to the `Switch` by setting the `on` prop.

#### Validate

This example shows how you can validate the `Switch` using the `react-hook-form`
package, which handles error messages. For connecting the form with the `Switch`
and validating, you need to register the field with custom error messages and
use the `useForm` hook from `react-hook-form`. Also, by using the `controlState`
prop, you can override the error messages and connect the `Switch`'s error state
and message to that of the form. This shows a hint in case of an error and
applies proper styling to the component.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Control the state
- Validate

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import { FieldSet, Switch } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    formState: { isSubmitSuccessful },
    control,
    reset,
  } = useForm<{
    'T&C': boolean;
  }>({
    mode: 'all',
    defaultValues: {
      'T&C': false,
    },
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="T&C"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Terms and conditions are required.',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FieldSet>
                <FieldSet.Legend>Terms and conditions:</FieldSet.Legend>
                <Switch
                  formValue="checked"
                  required
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                >
                  I agree to the terms and conditions
                </Switch>
              </FieldSet>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import { FieldSet, Switch } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    formState: { isSubmitSuccessful },
    control,
    reset,
  } = useForm<{
    'T&C': boolean;
  }>({
    mode: 'all',
    defaultValues: {
      'T&C': false,
    },
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="T&C"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Terms and conditions are required.',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FieldSet>
                <FieldSet.Legend>Terms and conditions:</FieldSet.Legend>
                <Switch
                  formValue="checked"
                  required
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint: error?.message,
                  }}
                  {...field}
                >
                  I agree to the terms and conditions
                </Switch>
              </FieldSet>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Props

The `Switch` component allows users to toggle between two different states. You
can set a specific initial value using the `defaultValue` prop for an
uncontrolled switch or setting the initial value of the state of a controlled
switch accordingly. The `name` prop also needs to be specified for identifying
the `Switch` when submitting it in a form.

#### SwitchProps

##### Signature:
`export declare type SwitchProps = ) => | > & & & & & & {
 /** The used as the value of the switch when submitting it in a form, if the switch is toggled on. */
 formValue?: ;
};`Still have questions?Find answers in the Dynatrace Community

---

## TextArea

`/design/components/forms/TextArea/`

The `TextArea` component can be used as a multi-line plain-text editing control
to enter free-form text, such as a comment on a form. The component uses a
fallback FormFieldMessages context if it wasn't wrapped in a FormField.

### Import

`tsx
import { TextArea } from '@dynatrace/strato-components/forms';
`

### Demo

This is the simplest version of the `TextArea` which is uncontrolled and
therefore handles its state internally. You can also set a specific initial
value using the `defaultValue` prop.

```tsx
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea />
    </FormField>
  );
};
```

```tsx
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea />
    </FormField>
  );
};
```


### Control state

The `TextArea` can also be controlled, meaning that you can handle the state. To
do so, you need to use the `onChange` prop to provide a handler that is called
when the internal state of the `TextArea` changes. You also need to assign the
value from the state to the `TextArea` by setting the `value` prop.

```tsx
import { useState } from 'react';

import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea value={value} onChange={setValue} />
    </FormField>
  );
};
```

```tsx
import { useState } from 'react';

import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea value={value} onChange={setValue} />
    </FormField>
  );
};
```


### Disable resizing

The `TextArea` component is resizable by default. However, in case you need to
disable resizing, you can set the `resize` prop to `none`. This doesn't change
the amount of text you can enter, but only the visual appearance. The amount of
text can be adjusted using the `cols` and `rows`.

```tsx
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const DisableResizing = () => {
  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea resize="none" />
    </FormField>
  );
};
```

```tsx
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const DisableResizing = () => {
  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea resize="none" />
    </FormField>
  );
};
```


### Restrict resizing to one direction

The `TextArea` component can be resized in both directions by default. However,
in case you need to resize in one direction only, you can set the `resize` prop
to `horizontal` or `vertical`.

```tsx
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const VerticalResize = () => {
  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea resize="vertical" />
    </FormField>
  );
};
```

```tsx
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';

const VerticalResize = () => {
  return (
    <FormField>
      <Label>Enter some feedback</Label>
      <TextArea resize="vertical" />
    </FormField>
  );
};
```


### Validation

This example shows how you can validate the `TextArea` using the
`react-hook-form` package, which handles error messages. For connecting the form
with the `TextArea` and validating, you need to register the field with custom
error messages and use the `useForm` hook from `react-hook-form`. Also, by using
the `controlState` prop, you can override the error messages and connect the
`TextArea`'s error state and message to that of the form. This shows a hint in
case of an error and applies proper styling to the component. The `minLength`
and `maxLength` can be set on the `TextArea` as props, as well as when
registering the field, to restrict the message length and show custom messages
if it doesn't match.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Disable resizing
- Restrict resizing to one direction
- Validation

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    control,
    handleSubmit,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    feedback: string;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="feedback"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Your feedback is required',
              },
              minLength: {
                value: 10,
                message: 'Feedback text cannot have less than 10 characters.',
              },
              maxLength: {
                value: 250,
                message: 'Feedback text cannot have more than 250 characters.',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Feedback</Label>
                <TextArea
                  minLength={10}
                  maxLength={250}
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint:
                      error?.message ||
                      'Please enter between 10 and 250 characters.',
                  }}
                  {...field}
                />
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import { FormField, Label, TextArea } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    control,
    handleSubmit,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    feedback: string;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="feedback"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Your feedback is required',
              },
              minLength: {
                value: 10,
                message: 'Feedback text cannot have less than 10 characters.',
              },
              maxLength: {
                value: 250,
                message: 'Feedback text cannot have more than 250 characters.',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Feedback</Label>
                <TextArea
                  minLength={10}
                  maxLength={250}
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint:
                      error?.message ||
                      'Please enter between 10 and 250 characters.',
                  }}
                  {...field}
                />
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Props

The `TextArea` component can be used as a multi-line plain-text editing control
to enter free-form text, such as a comment on a form. The component uses a
fallback FormFieldMessages context if it wasn't wrapped in a FormField.

#### TextAreaProps

##### Signature:
`export declare type TextAreaProps = ) => | > & & & & & & & {
 placeholder?: ;
 /**
 * This attribute indicates whether the textarea is resizable by the user, and, if so, in which direction.
 * @defaultValue
 */
 resize?: | | | ;
 /**
 * The visible width of the text control, in average character widths.
 * If it is specified, it must be a positive integer.
 * @defaultValue 20
 */
 cols?: ;
 /**
 * The of visible text lines for the control. If it is specified, it must be a positive integer.
 * @defaultValue 2
 */
 rows?: ;
 /**
 * The minimum of characters required that the user should enter.
 * Doesn't stop the user from removing characters so that the entered goes past the minimum,
 * but it does make the value entered into the invalid.
 * With a set minlength an empty is still considered valid unless you also have the required attribute set.
 */
 minLength?: ;
 /**
 * The maximum of characters that the user can enter. If this value isn't specified,
 * the user can enter an unlimited of characters.
 */
 maxLength?: ;
 /**
 * This attribute indicates whether the value of the control can be automatically completed by the browser.
 * If no autocompletion is desired, it can be set to .
 */
 autoComplete?: ;
 /**
 * Sets the width of the textarea element.
 * @defaultValue
 */
 width?: | | .>;
};`Still have questions?Find answers in the Dynatrace Community

---

## TextInput

`/design/components/forms/TextInput/`

Use the `TextInput` component to request a small amount of information, such as
a name or an email address. To let users input larger amounts of text, use a
`TextArea` instead.

### Import

`tsx
import { TextInput } from '@dynatrace/strato-components/forms';
`

### Demo

This is the simplest version of the `TextInput`, which is uncontrolled and
therefore handles its state internally. You can also set a specific initial
value using the `defaultValue` prop.

```tsx
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Enter text</Label>
      <TextInput />
    </FormField>
  );
};
```

```tsx
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';

const Basic = () => {
  return (
    <FormField>
      <Label>Enter text</Label>
      <TextInput />
    </FormField>
  );
};
```


### Control state

The `TextInput` can also be controlled, meaning that you can handle the state.
To do so, you need to use the `onChange` prop to provide a handler that is
called when the internal state of the `TextInput` changes. You also need to
assign the value from the state to the `TextInput` by setting the `value` prop.

```tsx
import { useState } from 'react';

import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Enter text</Label>
      <TextInput value={value} onChange={setValue} />
    </FormField>
  );
};
```

```tsx
import { useState } from 'react';

import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';

const Controlled = () => {
  const [value, setValue] = useState('');

  return (
    <FormField>
      <Label>Enter text</Label>
      <TextInput value={value} onChange={setValue} />
    </FormField>
  );
};
```


### Add prefix or suffix

You can add a prefix or a suffix to the `TextInput`, which can render an icon or
a `TextInput.Button` with a click handler. When using the `TextInput.Button`
that renders an icon or any similar element without any text, you need to add
either the `aria-label` prop or the `tooltipText` prop to provide a text
description for the button.

```tsx
import { useRef, useState } from 'react';

import {
  FormField,
  FormControlRef,
  TextInput,
  Label,
} from '@dynatrace/strato-components/forms';
import { FilterIcon, SettingIcon, XmarkIcon } from '@dynatrace/strato-icons';

const PrefixSuffix = () => {
  const [value, setValue] = useState('');
  const inputRef = useRef<FormControlRef<HTMLDivElement>>(null);

  return (
    <FormField>
      <Label>Enter text</Label>
      <TextInput
        placeholder="Enter something"
        value={value}
        onChange={setValue}
        ref={inputRef}
      >
        <TextInput.Prefix>
          <FilterIcon aria-label="Filter" />
        </TextInput.Prefix>
        <TextInput.Suffix>
          <SettingIcon aria-label="Settings" />
          <TextInput.Button
            onClick={() => {
              setValue('');
              inputRef.current?.inputRef?.focus();
            }}
          >
            <XmarkIcon />
          </TextInput.Button>
        </TextInput.Suffix>
      </TextInput>
    </FormField>
  );
};
```

```tsx
import { useRef, useState } from 'react';

import {
  FormField,
  FormControlRef,
  TextInput,
  Label,
} from '@dynatrace/strato-components/forms';
import { FilterIcon, SettingIcon, XmarkIcon } from '@dynatrace/strato-icons';

const PrefixSuffix = () => {
  const [value, setValue] = useState('');
  const inputRef = useRef<FormControlRef<HTMLDivElement>>(null);

  return (
    <FormField>
      <Label>Enter text</Label>
      <TextInput
        placeholder="Enter something"
        value={value}
        onChange={setValue}
        ref={inputRef}
      >
        <TextInput.Prefix>
          <FilterIcon aria-label="Filter" />
        </TextInput.Prefix>
        <TextInput.Suffix>
          <SettingIcon aria-label="Settings" />
          <TextInput.Button
            onClick={() => {
              setValue('');
              inputRef.current?.inputRef?.focus();
            }}
          >
            <XmarkIcon />
          </TextInput.Button>
        </TextInput.Suffix>
      </TextInput>
    </FormField>
  );
};
```


### Variants

The `TextInput` can be styled differently using the `variant` prop. The default
visual representation is `default`, but can also be set to `minimal`.

```tsx
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex gap={8}>
      <Flex>
        <FormField>
          <Label>Enter text</Label>
          <TextInput placeholder="This is a default text input" />
        </FormField>
      </Flex>
      <Flex>
        <FormField>
          <Label>Enter text</Label>
          <TextInput
            placeholder="This is a minimal text input"
            variant="minimal"
          />
        </FormField>
      </Flex>
    </Flex>
  );
};
```

```tsx
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Variants = () => {
  return (
    <Flex gap={8}>
      <Flex>
        <FormField>
          <Label>Enter text</Label>
          <TextInput placeholder="This is a default text input" />
        </FormField>
      </Flex>
      <Flex>
        <FormField>
          <Label>Enter text</Label>
          <TextInput
            placeholder="This is a minimal text input"
            variant="minimal"
          />
        </FormField>
      </Flex>
    </Flex>
  );
};
```


### Make input read-only

The `TextInput` can be set to read-only by simply adding the `readOnly` prop.

```tsx
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';

const ReadOnly = () => {
  return (
    <FormField>
      <Label>Read-only</Label>
      <TextInput readOnly defaultValue="This text is read-only" />
    </FormField>
  );
};
```

```tsx
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';

const ReadOnly = () => {
  return (
    <FormField>
      <Label>Read-only</Label>
      <TextInput readOnly defaultValue="This text is read-only" />
    </FormField>
  );
};
```


### Validation

This example shows how you can validate the `TextInput` using the
`react-hook-form` package, which handles error messages. For connecting the form
with the `TextInput` and validating, you need to register the field with custom
error messages and use the `useForm` hook from `react-hook-form`. Also, by using
the `controlState` prop, you can override the error messages and connect the
`TextInput`'s error state and message to that of the form. This shows a hint in
case of an error and applies proper styling to the component. The `minLength`
and `maxLength` can be set on the `TextInput` as props, as well as when
registering the field, to restrict the message length and show custom messages
if it doesn't match. You can also use the `pattern` prop to provide a RegEx that
defines which characters are allowed.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Add prefix or suffix
- Variants
- Make input read-only
- Validation

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{ username: string }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="username"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Please enter a username.',
              },
              minLength: {
                value: 5,
                message: 'The username cannot have less than 5 characters.',
              },
              maxLength: {
                value: 20,
                message: 'The username cannot have more than 20 characters.',
              },
              pattern: {
                value: /^[a-zA-Z].*\d[A-Za-z\d]+/,
                message: 'The username must contain numbers and characters',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Username</Label>
                <TextInput
                  placeholder="Enter your username"
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint:
                      error?.message ||
                      'Please enter between 5 and 20 characters.',
                  }}
                  {...field}
                />
              </FormField>
            )}
          />

          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FormField,
  Label,
  TextInput,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validation = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{ username: string }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="username"
            control={control}
            rules={{
              required: {
                value: true,
                message: 'Please enter a username.',
              },
              minLength: {
                value: 5,
                message: 'The username cannot have less than 5 characters.',
              },
              maxLength: {
                value: 20,
                message: 'The username cannot have more than 20 characters.',
              },
              pattern: {
                value: /^[a-zA-Z].*\d[A-Za-z\d]+/,
                message: 'The username must contain numbers and characters',
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <Label>Username</Label>
                <TextInput
                  placeholder="Enter your username"
                  controlState={{
                    state: error ? 'error' : 'valid',
                    hint:
                      error?.message ||
                      'Please enter between 5 and 20 characters.',
                  }}
                  {...field}
                />
              </FormField>
            )}
          />

          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Props

Use the `TextInput` component to request a small amount of information, such as
a name or an email address. To let users input larger amounts of text, use a
`TextArea` instead.

#### TextInputProps

##### Signature:
`export declare type TextInputProps = & ) => > & & & {
 /**
 * Maps to the native input type. Use this to enhance the semantics
 * of the native input, change default keyboards on mobile or support browser
 * autocompletion for specific types.
 * @see {@link https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types}
 *
 * @defaultValue
 */
 type?: | | | | | ;
};`

#### TextInputUncontrolledProps
Deprecated

- please use TextInputProps instead.
 |
 | Name | Type | Default | Description
 | `defaultValue?` | | | The default value of the input.

#### TextInputControlledProps
Deprecated

- please use TextInputProps instead.
 |
 | Name | Type | Default | Description
 | `value?` | | | The value of the input.

#### TextInput.Prefix, TextInput.Suffix

You can use the `TextInput.Prefix` component to render custom content in front
of the input, or the `TextInput.Suffix` component if you need to render content
after it.

Prop Table did not receive data

#### TextInput.Button

You can use the `TextInput.Button` component to render a button inside the
`TextInput.Prefix` or `TextInput.Suffix` component.

Prop Table did not receive dataStill have questions?Find answers in the Dynatrace Community
- TextInput.Prefix, TextInput.Suffix
- TextInput.Button

---

## ToggleButtonGroup

`/design/components/forms/ToggleButtonGroup/`

`ToggleButtonGroup` lets users toggle between a set of related options,
typically with one preselected. It's best for switching between views or a
compact group of options with immediate effect.

### Import

`tsx
import { ToggleButtonGroup } from '@dynatrace/strato-components/forms';
`

### Use cases

#### Control the state

The `ToggleButtonGroup` supports controlled behavior, enabling direct management
of its state. This is achieved by passing a handler to the `onChange` prop,
which is invoked whenever the internal state changes. The updated state can then
be passed to the `value` prop to apply the new selection.

#### Icons

Icons can be placed before or after the text in the `ToggleButtonGroup.Item`. If
an item only displays an icon, include a `tooltip` describing what the icon
represents.

```tsx
import { ToggleButtonGroup } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  ColumnsIcon,
  LegendBottomIcon,
  LegendRightIcon,
  RowsIcon,
  SecurityCriticalIcon,
  SecurityHighIcon,
  SecurityMediumIcon,
  WarningIcon,
} from '@dynatrace/strato-icons';

const Icons = () => {
  return (
    <Flex flexDirection="column" gap={8}>
      <div>
        <ToggleButtonGroup name="item-only">
          <ToggleButtonGroup.Item
            value="legend-right"
            tooltip="Legend Right"
            data-testid="legend-right"
            aria-label="Legend Right"
          >
            <ToggleButtonGroup.Prefix>
              <LegendRightIcon />
            </ToggleButtonGroup.Prefix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item
            value="legend-bottom"
            tooltip="Legend Bottom"
            data-testid="legend-bottom"
            aria-label="Legend Bottom"
          >
            <ToggleButtonGroup.Suffix>
              <LegendBottomIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item
            value="columns"
            tooltip="Columns"
            data-testid="columns"
            aria-label="Columns"
          >
            <ToggleButtonGroup.Suffix>
              <ColumnsIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item
            value="rows"
            tooltip="Rows"
            data-testid="rows"
            aria-label="Rows"
          >
            <ToggleButtonGroup.Suffix>
              <RowsIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup name="prefix-suffix">
          <ToggleButtonGroup.Item value="critical">
            <ToggleButtonGroup.Prefix>
              <SecurityCriticalIcon />
            </ToggleButtonGroup.Prefix>
            Security Critical
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="high">
            <ToggleButtonGroup.Prefix>
              <SecurityHighIcon />
            </ToggleButtonGroup.Prefix>
            Security High
            <ToggleButtonGroup.Suffix>
              <WarningIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="medium">
            <ToggleButtonGroup.Prefix>
              <SecurityMediumIcon />
            </ToggleButtonGroup.Prefix>
            Security Medium
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
    </Flex>
  );
};
```

```tsx
import { ToggleButtonGroup } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  ColumnsIcon,
  LegendBottomIcon,
  LegendRightIcon,
  RowsIcon,
  SecurityCriticalIcon,
  SecurityHighIcon,
  SecurityMediumIcon,
  WarningIcon,
} from '@dynatrace/strato-icons';

const Icons = () => {
  return (
    <Flex flexDirection="column" gap={8}>
      <div>
        <ToggleButtonGroup name="item-only">
          <ToggleButtonGroup.Item
            value="legend-right"
            tooltip="Legend Right"
            data-testid="legend-right"
            aria-label="Legend Right"
          >
            <ToggleButtonGroup.Prefix>
              <LegendRightIcon />
            </ToggleButtonGroup.Prefix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item
            value="legend-bottom"
            tooltip="Legend Bottom"
            data-testid="legend-bottom"
            aria-label="Legend Bottom"
          >
            <ToggleButtonGroup.Suffix>
              <LegendBottomIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item
            value="columns"
            tooltip="Columns"
            data-testid="columns"
            aria-label="Columns"
          >
            <ToggleButtonGroup.Suffix>
              <ColumnsIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item
            value="rows"
            tooltip="Rows"
            data-testid="rows"
            aria-label="Rows"
          >
            <ToggleButtonGroup.Suffix>
              <RowsIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup name="prefix-suffix">
          <ToggleButtonGroup.Item value="critical">
            <ToggleButtonGroup.Prefix>
              <SecurityCriticalIcon />
            </ToggleButtonGroup.Prefix>
            Security Critical
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="high">
            <ToggleButtonGroup.Prefix>
              <SecurityHighIcon />
            </ToggleButtonGroup.Prefix>
            Security High
            <ToggleButtonGroup.Suffix>
              <WarningIcon />
            </ToggleButtonGroup.Suffix>
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="medium">
            <ToggleButtonGroup.Prefix>
              <SecurityMediumIcon />
            </ToggleButtonGroup.Prefix>
            Security Medium
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
    </Flex>
  );
};
```


#### Disable options

The `ToggleButtonGroup` offers two disable options. You can disable the entire
group or disable specific buttons. To implement either option, apply the
`disabled` prop to the target element (either the group or an individual
button).

```tsx
import { ToggleButtonGroup } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Disabled = () => {
  return (
    <Flex flexDirection="column" gap={8}>
      <div>
        <ToggleButtonGroup disabled name="disabled">
          <ToggleButtonGroup.Item value="all">
            All options
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="disabled">
            disabled
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup name="item-disabled">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item disabled value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
    </Flex>
  );
};
```

```tsx
import { ToggleButtonGroup } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Disabled = () => {
  return (
    <Flex flexDirection="column" gap={8}>
      <div>
        <ToggleButtonGroup disabled name="disabled">
          <ToggleButtonGroup.Item value="all">
            All options
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="disabled">
            disabled
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup name="item-disabled">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item disabled value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
    </Flex>
  );
};
```


#### Width

The `width` property of the `ToggleButtonGroup` component accepts three types of
values:

- `content`: adjusts the width to fit the content,

- `full`: expands to the full available width,

- Custom string values (e.g., "400px"): allows specifying an exact width.

```tsx
import { ToggleButtonGroup } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Width = () => {
  return (
    <Flex flexDirection="column" gap={8}>
      <div>
        <ToggleButtonGroup width="content" name="content">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup width="600px" name="600px">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup width="full" name="full">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
    </Flex>
  );
};
```

```tsx
import { ToggleButtonGroup } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const Width = () => {
  return (
    <Flex flexDirection="column" gap={8}>
      <div>
        <ToggleButtonGroup width="content" name="content">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup width="600px" name="600px">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
      <div>
        <ToggleButtonGroup width="full" name="full">
          <ToggleButtonGroup.Item value="left">
            align left
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="center">
            align center
          </ToggleButtonGroup.Item>
          <ToggleButtonGroup.Item value="right">
            align right
          </ToggleButtonGroup.Item>
        </ToggleButtonGroup>
      </div>
    </Flex>
  );
};
```


#### Validation

The `ToggleButtonGroup` supports an error state, which can be triggered in two
primary ways:

- Form submission: If the form containing the `ToggleButtonGroup` is submitted
with invalid or missing data, the component can reflect the error state.

- Validation function: Validation logic can be applied to determine whether the
selected value meets the required criteria.

This example demonstrates how to show users an validation message using
`FormFieldMessages`.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Control the state
- Icons
- Disable options
- Width
- Validation

```tsx
import { useState, useRef } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  ToggleButtonGroup,
  type FormControlRef,
  FormField,
  Label,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  LineChartIcon,
  BandChartIcon,
  GanttChartIcon,
} from '@dynatrace/strato-icons';

const Validation = () => {
  const toggleButtonGroupRef = useRef<FormControlRef<HTMLDivElement>>(null);
  const [showCustomError, setShowCustomError] = useState(false);

  return (
    <Flex flexDirection="column">
      <form
        onSubmit={(event) => {
          event.preventDefault();
        }}
      >
        <FormField>
          <Label>ToggleButtonGroup</Label>
          <ToggleButtonGroup ref={toggleButtonGroupRef} name="form" required>
            <ToggleButtonGroup.Item value="line-chart">
              <ToggleButtonGroup.Prefix>
                <LineChartIcon />
              </ToggleButtonGroup.Prefix>
              Line Chart
            </ToggleButtonGroup.Item>
            <ToggleButtonGroup.Item value="bar-chart">
              <ToggleButtonGroup.Prefix>
                <BandChartIcon />
              </ToggleButtonGroup.Prefix>
              Bar Chart
            </ToggleButtonGroup.Item>
            <ToggleButtonGroup.Item value="gant-chart">
              <ToggleButtonGroup.Prefix>
                <GanttChartIcon />
              </ToggleButtonGroup.Prefix>
              Gant Chart
            </ToggleButtonGroup.Item>
          </ToggleButtonGroup>
          <FormFieldMessages>
            {(messages) => {
              if (showCustomError) {
                return (
                  <FormFieldMessages.Item variant="error">
                    Custom error for the radio group
                  </FormFieldMessages.Item>
                );
              }
              if (!messages || messages.length === 0) {
                return (
                  <FormFieldMessages.Item variant="hint">
                    Please select an Item
                  </FormFieldMessages.Item>
                );
              }
              return messages.map((msg) => (
                <FormFieldMessages.Item key={msg.id} {...msg} />
              ));
            }}
          </FormFieldMessages>
        </FormField>
        <Button variant="accent" type="submit">
          Submit
        </Button>
        <Button
          variant="emphasized"
          onClick={() => setShowCustomError(!showCustomError)}
        >
          Toggle custom error
        </Button>
      </form>
    </Flex>
  );
};
```

```tsx
import { useState, useRef } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  ToggleButtonGroup,
  type FormControlRef,
  FormField,
  Label,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  LineChartIcon,
  BandChartIcon,
  GanttChartIcon,
} from '@dynatrace/strato-icons';

const Validation = () => {
  const toggleButtonGroupRef = useRef<FormControlRef<HTMLDivElement>>(null);
  const [showCustomError, setShowCustomError] = useState(false);

  return (
    <Flex flexDirection="column">
      <form
        onSubmit={(event) => {
          event.preventDefault();
        }}
      >
        <FormField>
          <Label>ToggleButtonGroup</Label>
          <ToggleButtonGroup ref={toggleButtonGroupRef} name="form" required>
            <ToggleButtonGroup.Item value="line-chart">
              <ToggleButtonGroup.Prefix>
                <LineChartIcon />
              </ToggleButtonGroup.Prefix>
              Line Chart
            </ToggleButtonGroup.Item>
            <ToggleButtonGroup.Item value="bar-chart">
              <ToggleButtonGroup.Prefix>
                <BandChartIcon />
              </ToggleButtonGroup.Prefix>
              Bar Chart
            </ToggleButtonGroup.Item>
            <ToggleButtonGroup.Item value="gant-chart">
              <ToggleButtonGroup.Prefix>
                <GanttChartIcon />
              </ToggleButtonGroup.Prefix>
              Gant Chart
            </ToggleButtonGroup.Item>
          </ToggleButtonGroup>
          <FormFieldMessages>
            {(messages) => {
              if (showCustomError) {
                return (
                  <FormFieldMessages.Item variant="error">
                    Custom error for the radio group
                  </FormFieldMessages.Item>
                );
              }
              if (!messages || messages.length === 0) {
                return (
                  <FormFieldMessages.Item variant="hint">
                    Please select an Item
                  </FormFieldMessages.Item>
                );
              }
              return messages.map((msg) => (
                <FormFieldMessages.Item key={msg.id} {...msg} />
              ));
            }}
          </FormFieldMessages>
        </FormField>
        <Button variant="accent" type="submit">
          Submit
        </Button>
        <Button
          variant="emphasized"
          onClick={() => setShowCustomError(!showCustomError)}
        >
          Toggle custom error
        </Button>
      </form>
    </Flex>
  );
};
```


### Props

`ToggleButtonGroup` lets users toggle between a set of related options,
typically with one preselected. It's best for switching between views or a
compact group of options with immediate effect.

#### ToggleButtonGroupProps

##### Signature:
`export declare type ToggleButtonGroupProps = ) => | > & & & & & & & {
 /**
 * The width of the ToggleButtonGroup.
 * @defaultValue
 */
 width?: | | ..;
};`

### Item

The `ToggleButtonGroup.Item` component is used to render individual elements
within the `ToggleButtonGroup`.

#### ToggleButtonGroupItemProps

##### Signature:
`export declare type ToggleButtonGroupItemProps = & & & & & & & {
 /** When a tooltip is provided, text is shown on hover. */
 tooltip?: ;
 /**
 * Zero or more items in a group can be checked.
 * @defaultValue false
 * @deprecated unused, will be removed
 */
 checked?: ;
 /**
 * Indicates if the mover is currently over the item.
 * @defaultValue false
 * @deprecated unused, will be removed
 */
 hovered?: ;
};`

### Prefix

The `ToggleButtonGroup.Prefix` component serves as a container for
manually-placed icons that appear before the text of the
`ToggleButtonGroup.Item`.

#### ToggleButtonGroupPrefixProps
extends`, , ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Button Prefix slot.

### Suffix

The `ToggleButtonGroup.Suffix` component serves as a container for
manually-placed icons that appear after the text of the
`ToggleButtonGroup.Item`.

#### ToggleButtonGroupSuffixProps
extends`, , ` |
 | Name | Type | Default | Description
 | `children` | | | Elements to be displayed in the Button Suffix slot.Still have questions?Find answers in the Dynatrace Community
- Item
- Prefix
- Suffix

---

