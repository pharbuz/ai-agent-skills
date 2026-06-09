# Develop — Reference

Scraped from <https://developer.dynatrace.com/develop/>. Each section is one doc page (its path is shown) with the prose and code captured.

## apis

`/develop/reference/apis/`

- API

## API

- Explanation
- 1-min readDynatrace offers a wide range of powerful APIs, which allow you to programmatically interact with the Dynatrace platform. They enable automation of daily routines and are available for both latest Dynatrace and Dynatrace classic.

There are different types of APIs available:

- Environment API—to view and update entities

- Configuration API—to manage Dynatrace configurations

- Account Management API—to manage users, permissions, and subscription details

### Discover our APIs

###

#### APIs for Dynatrace classic
An overview of all of our APIs for the previous Dynatrace.

#### APIs for latest Dynatrace
An overview of all of our APIs for the latest Dynatrace.

---

## apis/classic-apis

`/develop/reference/apis/classic-apis/`

- API
- APIs for Dynatrace classic

## APIs for Dynatrace classic
See this list of all APIs available for Dynatrace Classic.

#### Environment API v1
Automate your monitoring tasks and export different types of data into your third-party reporting and analysis tools.

#### Basics
Learn about the basics, such as authentication, response codes, and rate limits.

#### Endpoints
Use components, design tokens, and icons from the Strato Design System to create a simple, intuitive, and beautiful app UI

#### API Explorer (Swagger)
Explore our Swagger definitions for each API to understand the structure and capabilities.

#### Account Experience API (Swagger)
Explore the Swagger definition for the Account Experience API.

---

## apis/latest-apis

`/develop/reference/apis/latest-apis/`

- API
- APIs for latest Dynatrace

## APIs for latest Dynatrace
The latest Dynatrace introduces several new concepts, use cases, and functionality. We recommend that you familiarize yourself with these first. Read all about them on our Best practices for upgrading to the latest Dynatrace page.

Here's a list of all APIs for Platform Services available for latest Dynatrace.

TipRead more about each Platform Service, and find our SDKs here.

#### AppEngine

#### AppEngine – App Functions
These functions represent the backend of an app and are built, bundled, and deployed together with your custom app.

#### AppEngine – EdgeConnect
Configures URL host patterns to securely forward HTTP requests from the Dynatrace runtime to private network resources via EdgeConnect

#### AppEngine – Function Executor
The function executor is an API that allows you to execute code (that you haven't bundled with apps) inside Dynatrace AppEngine.

#### AppEngine – Registry
The Registry is mainly responsible for installing, updating, storing apps, uninstalling, removing apps, and getting apps.

#### AutomationEngine

#### Automation
Manage and run workflows with the AutomationEngine API.

#### Classic environment

#### Environment API v1
Automate your monitoring tasks and export different types of data into your third-party reporting and analysis tools.

#### Environment API v2
Automate your monitoring tasks and export different types of data into your third-party reporting and analysis tools.

#### Configuration API
Manage and keep track of your Dynatrace monitoring environment configurations.

#### Davis AI

#### Davis AI – Predictive and Causal
Explore our Davis AI – Predictive and Causal API.

#### Davis CoPilot – Generative AI (Preview)
This API allows you to interact with Davis CoPilot Generative AI. The API is in preview and is subject to the Dynatrace preview conditions.

#### Document

#### Document Service
This API allows you to create and manage documents, as well as manage access to them.

#### Email

#### Email
APIs that allow sending emails.

#### Grail

#### Grail – DQL Query
Exposes an API to fetch records stored in Grail.

#### Grail – Fieldsets
Fieldset management for Grail.

#### Grail – Filter Segments
Filter-Segment Management for Grail. Slice, dice and contextualize your data to make it easier to find, understand and work with.

#### Grail – Resource Store
The Resource Store API uses the Dynatrace Pattern Language to parse uploaded data and convert it into a tabular storage format.

#### Grail – Storage Management
This API allows you to manage storage for Grail. Data is organizied in buckets.

#### Grail – Storage Record Deletion
The record deletion API is primarily designed to help users remove selected records containing sensitive data.

#### Hub

#### Hub
The Hub API provides catalog content, such as Dynatrace Apps, Extensions, and Technologies, in the context of the current environment.

#### Identity and Access Management

#### Identity and Access Management
Identity and Access Management configuration. Allows viewing users within the platform and their access capabilities.

#### Notification

#### Notification v1
Manage self notifications with the Notification Service API. This is deprecated, use event notifications provided in the Notification Service v2 API instead.

#### Notification v2
Manage resource/event notifications with the Notification Service API.

#### OpenPipeline

#### OpenPipeline
Fetch and update OpenPipeline configurations for different data sources.

#### OpenPipeline – Ingest API
Ingest generic events to OpenPipeline configurations for different data sources.

#### Platform management

#### Platform Management
Basic read-only information about the currently logged-in environment.

#### Service-Level Objectives

#### Service-Level Objectives
Management API for service-level objectives, templates and evaluating service-level objectives.

#### State service

#### State Management
Provides key-value storage for apps so that app developers can persist and get small chunks of state in the context of their app.

#### Vulnerabilities

#### Vulnerabilities
APIs that manage vulnerability related information.

---

## javascript-runtime

`/develop/reference/javascript-runtime/`

- JavaScript runtime

## JavaScript runtime

- 4-min readThe app functions you create for your app run within the Dynatrace JavaScript runtime.
This page documents available JavaScript objects, WebAPIs, and packages of the SDK for TypeScript the runtime provides to write app functions.

### SDK for TypeScript

The SDK for TypeScript can be used to access Dynatrace platform services and Dynatrace AppEngine functionality.

### Standard built-in objects

The Dynatrace JavaScript runtime supports all standard JavaScript built-ins and the ECMAScript Internationalization API. For a list of available objects, visit the standard built-objects documentation on MDN (Mozilla Developer Network).

### Web APIs

Web APIs are fundamental building blocks when writing web applications. Below is a list of all the APIs and interfaces (object types) available within the Dynatrace JavaScript runtime. To learn more about these APIs, visit Web API docs on MDN.

CautionDeprecated properties of Web APIs might not be supported.

- `AbortController`

- `AbortSignal`

- `atob`

- `Blob`

- `btoa`

- `ByteLengthQueuingStrategy`

- `clearInterval`

- `clearTimeout`

- `CompressionStream` (currently only supported in deployed apps, not in local development)

- `console`

- `CountQueuingStrategy`

- `Crypto`

- `crypto`

- `CryptoKey`

- `CustomEvent`

- `DecompressionStream` (currently only supported in deployed apps, not in local development)

- `DOMException`

- `ErrorEvent`

- `Event`

- `EventTarget`

- `fetch`

- `File`

- `FileReader`

- `FormData`

- `Headers`

- `Location`

- `location`

- `Navigator`

- `navigator`

- `Performance`

- `performance`

- `PerformanceEntry`

- `PerformanceMark`

- `PerformanceMeasure`

- `ProgressEvent`

- `PromiseRejectionEvent`

- `ReadableByteStreamController`

- `ReadableStream`

- `ReadableStreamBYOBReader`

- `ReadableStreamBYOBRequest`

- `ReadableStreamDefaultController`

- `ReadableStreamDefaultReader`

- `reportError`

- `Request`

- `Response`

- `setInterval`

- `setTimeout`

- `structuredClone`

- `SubtleCrypto`

- `TextDecoder`

- `TextDecoderStream`

- `TextEncoder`

- `TextEncoderStream`

- `TransformStream`

- `TransformStreamDefaultController`

- `URL`

- `URLPattern`

- `URLSearchParams`

- `Window`

- `window`

- `WritableStream`

- `WritableStreamDefaultController`

- `WritableStreamDefaultWriter`

### Node.js compatibility

The Dynatrace JavaScript runtime provides a compatibility layer for Node.js to improve compatibility with third-party npm packages.

CautionNode.js compatibility is subject to limitations, and third-party packages that rely on operations such as TCP (Transmission Control Protocol)/UDP (User Datagram Protocol) socket or file system access aren't supported.
Built-in modules in the compatibility layer might miss certain functionality from their Node.js counterparts.Most functionality exposed in the Node.js compatibility layer is also available via Web APIs.
We recommend using Web APIs such as `fetch` instead of Node.js modules like `http` where possible.

#### Available modules

The following built-in Node.js modules are available. Note that the list of limitations is non-exhaustive and subject to changes in the future.

 |
 | Module | Description | Limitations
 | `assert/strict`,
`assert` | Node.js assertions |
 | `buffer` | Node.js-specific extensions to `Uint8Array` |
 | `console` | Logging capabilities (e.g. `console.log`) |
 | `crypto` | Cryptographic functionality such as hashing and encryption | Certain algorithms, custom certificates and Diffie-Hellman key exchanges aren't supported
 | `events` | Utilities around event emitters and listeners |
 | `http` | HTTP server and client functionality over plain text | Creating an HTTP server isn't supported
 | `https` | HTTP server and client functionality over TLS (Transport Layer Security) | Creating an HTTP server isn't supported
 | `path` | Utilities for working with file and directory paths |
 | `perf_hooks` | Performance measurement APIs | Some functionality isn't implemented:
- `performance.timerify`
- `performance.eventLoopUtilization`
- `performance.monitorEventLoopDelay`
 | `querystring` | Utilities for parsing and formatting URL query strings |
 | `stream`,
`stream/consumers`,
`stream/promises` | APIs for streaming data |
 | `stream/web` | An implementation of the WHATWG Streams Standard |
 | `string_decoder` | APIs for decoding UTF-8 and UTF-16 data from streams | Unsupported encodings:
- `ascii`
- `utf16le`
- `latin1`
 | `timers`,
`timers/promises` | API for scheduling functions to be called in the future |
 | `url` | Utilities for URL resolution and parsing |
 | `util` | Various utilities for application development |
 | `zlib` | Compression and decompression utilities | Brotli compression isn't implemented

#### Stubbed modules

You can import the following modules to ensure compatibility with specific third-party packages, but all exposed functions throw errors when called.

 |
 | Module | Description
 | `process` | Provides information about the current process
 | `fs`,
`fs/promises` | File system operations

#### Deprecations

The following functionalities are deprecated and will be removed with a future release of the Dynatrace JavaScript runtime. Please refrain from using them and be aware that third-party dependencies using the functionalities might break once they are removed.

 |
 | Functionality | Reason for deprecation
 | `globalThis.window` | Was used to wrongly determine that code is executed in a browser.
 | `eval("...")` | Security risk: executes arbitrary strings as code, which can lead to remote code execution if the input contains untrusted data (for example, dashboard variables sourced from logs or user-provided query parameters).
 | `new Function("...")` | Security risk: constructs and executes a function from a string, identical risk to `eval()`.

### Runtime limitations

The following restrictions currently apply to functions:

- Function execution times out after 120 seconds.

- Functions can't call functions of other apps.

- Functions can't call the function executor API.

- Functions are deployed in an environment with 256 MB of RAM.

- Functions can't send binary responses.

- Function inputs and outputs can't be larger than 5 MB, respectively.

- There's a limit on concurrent requests you can make to app functions. You'll get the 429 Too Many Requests HTTP response status code when you reach the limit.

- Calls to external hosts need to be explicitly allowed. See how to allow outbound connections.

- You can't use WebSocket API in app functions. See the available APIs.

---

## metric-units

`/develop/reference/metric-units/`

- Metric units

## Metric units

- 6-min readMetric units are used in data visualizations and are available for custom use and conversions in the @dynatrace-sdk/units.

### SI Prefixes

 |
 | Name | Symbol | English word | Scientific Notation
 | quetta | Q | nonillion | 10^30
 | ronna | R | octillion | 10^27
 | yotta | Y | septillion | 10^24
 | zetta | Z | sextillion | 10^21
 | exa | E | quintillion | 10^18
 | peta | P | quadrillion | 10^15
 | tera | T | trillion | 10^12
 | giga | G | billion | 10^9
 | mega | M | million | 10^6
 | kilo | k | thousand | 10^3
 | hecto | h | hundred | 10^2
 | deca | da | ten | 10^1
 | | | one | 10^0
 | deci | d | tenth | 10^-1
 | centi | c | hundredth | 10^-2
 | milli | m | thousandth | 10^-3
 | micro | µ | millionth | 10^-6
 | nano | n | billionth | 10^-9
 | pico | p | trillionth | 10^-12
 | femto | f | quadrillionth | 10^-15
 | atto | a | quintillionth | 10^-18
 | zepto | z | sextillionth | 10^-21
 | yocto | y | septillionth | 10^-24
 | ronto | r | octillionth | 10^-27
 | quecto | q | nonillionth | 10^-30

### Angle

 |
 | Name | Symbol
 | milliradian | mrad
 | radian | rad
 | second | ″
 | minute | ′
 | degree | °
 | revolution | r

### Area

 |
 | Name | Symbol
 | square meter | m^2
 | square inch | in^2
 | square foot | ft^2
 | square yard | yd^2
 | square mile | mi^2

### Currency

 |
 | Name | Symbol
 | US Dollar | US$
 | Euro | €
 | Japanese Yen | ¥
 | British Pound | £
 | Australian Dollar | A$
 | Canadian Dollar | C$
 | New Zealand Dollar | NZ$
 | Swiss Franc | CHF
 | Chinese Yuan | 元

### Data

 |
 | Name | Symbol
 | bit | bit
 | kilobit | kbit
 | megabit | Mbit
 | gigabit | Gbit
 | ... |
 | byte | B
 | kilobyte | kB
 | megabyte | MB
 | gigabyte | GB
 | terabyte | TB
 | petabyte | PB
 | ... |
 | kibibyte | KiB
 | mebibyte | MiB
 | gibibyte | GiB
 | tebibyte | TiB
 | pebibyte | PiB
 | ... |

### Datarate

 |
 | Name | Symbol
 | bitps | bit/s
 | kbitpm | kbit/min
 | kBph | kB/h
 | ... |
 | kiBps | KiB/s
 | Mbitps | Mbit/s
 | Gbitps | Gbit/s
 | ... |
 | Mibitps | Mibit/s
 | Gibitpm | Gibit/min
 | ... |

### Electricity

 |
 | Name | Symbol
 | ampere | A
 | volt | V
 | ohm | Ω
 | watt | W
 | coulomb | C
 | farad | F
 | weber | Wb
 | tesla | T
 | henry | H
 | siemens | S

### Force

 |
 | Name | Symbol
 | newton | N
 | pound | lbf

### Frequency

 |
 | Name | Symbol
 | hertz | Hz

### Length

 |
 | Name | Symbol
 | meter | m
 | inch | in
 | foot | ft
 | yard | yd
 | mile | mi
 | astronomical unit | au
 | lightyear 🚀 | ly

### Mass

 |
 | Name | Symbol
 | gram | g
 | grain | gr
 | ounce | oz
 | pound | lb
 | tonne | t

### Percentage

 |
 | Name | Symbol
 | promille | ‰
 | percent | %
 | one | x

### Physics

 |
 | Name | Symbol
 | gray | Gy
 | sievert | Sv
 | candela | cd
 | lumen | lm
 | lux | lx
 | steradian | sr

### Pressure

 |
 | Name | Symbol
 | pascal | Pa
 | psi | psi
 | bar | bar

### Temperature

 |
 | Name | Symbol
 | kelvin | K
 | degree celsius | °C
 | degree fahrenheit | °F
 | degree rankine | °R

### Time

 |
 | Name | Symbol
 | second | s
 | day | D
 | week | W
 | month | M
 | year | Y
 | hour | h
 | minute | min

### Unspecified

 |
 | Name | Symbol
 | count | count
 | count per second | count/s
 | count per minute | count/min
 | count per hour | count/h
 | core | core
 | millicore | millicore
 | msu | MSU
 | pixel | px
 | ratio | ratio
 | state | state
 | unspecified | unspecified
 | none |

### Velocity

 |
 | Name | Symbol
 | kilometer per hour | km/h
 | meter per second | m/s
 | miles per hour | mi/h

### Volume

 |
 | Name | Symbol
 | cubic meter | m^3
 | litre | dm^3
 | cubic inch | in^3
 | cubic feet | ft^3

---

## react-components/automation-action

`/develop/reference/react-components/automation-action/`

- React components
- Automation action

## Automation action components

- 1-min readThe React automation components in this section complement Strato and are helpful for building workflow action widgets. They support auto-completion for consuming the results of earlier executed tasks and expressions.

---

## react-components/automation-action/AutomationCodeEditor

`/develop/reference/react-components/automation-action/AutomationCodeEditor/`

- React components
- Automation action

## AutomationCodeEditor

- 2-min readThe `AutomationCodeEditor` provides a text input field specifically designed for editing code. Furthermore, it offers properties to configure, for example, syntax highlighting, spell checks, or line wrapping. Upon selecting the editor in the browser, the user can start editing by pressing the `Enter` key and can quit and return to the keyboard navigation flow by pressing the `Escape` key.

### Import

`tsx
import { AutomationCodeEditor } from '@dynatrace/automation-action-components';
`

### Props

Prop Table did not receive data

---

## react-components/automation-action/AutomationConnectionPicker

`/develop/reference/react-components/automation-action/AutomationConnectionPicker/`

- React components
- Automation action

## AutomationConnectionPicker

- 2-min readThe `AutomationConnectionPicker` allows users to select a single settings object. The available options will be fetched and displayed according to the given settings `schema`. Users can also create new settings objects with the Create a new connection link and can edit the objects by selecting Edit.

### Import

`tsx
import { AutomationConnectionPicker } from '@dynatrace/automation-action-components';
`

### Props

Prop Table did not receive data

---

## react-components/automation-action/AutomationSelect

`/develop/reference/react-components/automation-action/AutomationSelect/`

- React components
- Automation action

## AutomationSelect

- 2-min readThe `AutomationSelect` component allows you to choose one or more options from a collapsed dropdown menu. Additionally, you can switch from select mode to expression mode, which displays an `AutomationTextInput`, for a dynamic expression.

### Import

`tsx
import { AutomationSelect } from '@dynatrace/automation-action-components';
`

### Props

The props are the same as for the Strato `Select` component.

Example.tsx
`tsx
import { AutomationSelect, Expression } from '@dynatrace/automation-action-components';export const Example = () => { const [value, setValue] = useStatestring | null | Expression>('{{ result("task_1").value_1 }}'); return ( AutomationSelect value={value} onChange={setValue}> SelectV2.Content>...SelectV2.Content> AutomationSelect> );};
`

---

## react-components/automation-action/AutomationTextInput

`/develop/reference/react-components/automation-action/AutomationTextInput/`

- React components
- Automation action

## AutomationTextInput

- 2-min readThe `AutomationTextInput` component allows you to provide regular text or a dynamic expression with auto-completion support.

### Import

`tsx
import { AutomationTextInput } from '@dynatrace/automation-action-components';
`

### Props

Prop Table did not receive data

---

## react-style-guide

`/develop/reference/react-style-guide/`

- React style guide

## React style guide

- 6-min readThis style guide is a set of best practices and guidelines for writing Dynatrace Apps. Even though the following is only a guide with no enforced rules, we highly recommend sticking to it to keep consistency across all Dynatrace Apps. You'll also see the link to eslint rules for most of the rules mentioned in this guide.

NoteThis style guide is a fork of Airbnb React style guide.

### Basic rules

- Only include one React component per file.

- However, multiple Stateless or Pure Components are allowed per file.

- Always use JSX syntax.

### Naming

- Extensions: Use `.tsx` extension for React components.

- Filename: Use PascalCase for filenames. For example, `ReservationCard.tsx`.

- Reference naming: Use PascalCase for React components and camelCase for their instances. eslint: `react/jsx-pascal-case`

Bad
`tsx
// componentimport fooBar from './FooBar';// instanceconst FooBar = FooBar />;
`

Good
`tsx
// componentimport FooBar from './FooBar';// instanceconst foobar = FooBar />;
`

- Hooks: Use camelCase for React hooks.

Bad
`tsx
export const UseFoo = () => { ... }
`

Good
`tsx
export const useFoo = () => { ... }
`

- Props Naming: Avoid using DOM component prop names for different purposes.

Detailed explanation
Why? People expect props like style and className to mean one specific thing. Varying this API for a subset of your app makes the code less readable and less maintainable, and may cause bugs.
Bad
`tsx
Foo style="fancy" />Foo className="fancy" />
`

Good
`tsx
Foo variant="fancy" />
`

### Quotes

- Always use double quotes (") for JSX attributes, but single quotes (') for all other JS. eslint: jsx-quotes

Detailed explanation
Why? Regular HTML attributes also typically use double quotes instead of single, so JSX attributes mirror this convention.
Bad
`tsx
Foo bar='bar' />Foo style={{ left: "20px" }} />
`

Good
`tsx
Foo bar="bar" />Foo style={{ left: '20px' }} />
`

### Props

- Always use camelCase for prop names, or PascalCase if the prop value is a React component.

Bad
`tsx
Foo UserName="hello" phone_number={12345678}/>
`

Good
`tsx
Foo userName="hello" phoneNumber={12345678} Component={SomeComponent}/>
`

- Omit the value of the prop when it's explicitly `true`. eslint: react/jsx-boolean-value

Bad
`tsx
Foo hidden={true} />
`

Good
`tsx
Foo hidden />
`

- Avoid using an array index as `key` prop, prefer a stable id. (Why?)

Bad
`tsx
todos.map((todo, index) => Todo {...todo} key={index} />);
`

Good
`tsx
todos.map((todo) => Todo {...todo} key={todo.id} />);
`

- Use spread props sparingly.

Detailed explanation
Why? Otherwise, you're more likely to pass unnecessary props down to components. For React v15.6.1 and older, you could pass invalid HTML attributes to the DOM.
Exceptions:

- Spreading objects with known, explicit props. This can be particularly useful when testing React components with Mocha's beforeEach construct.

`tsx
export default function Foo() { const props = { text: '', isPublished: false, }; return div {...props} />;}
`

- To filter out unnecessary props when possible.

Caution
`tsx
export const Foo = (props) => { return Bar {...props} />;};
`

Better
`tsx
// filter out unnecessary propsexport const Foo = (props) => { const { ignoredProp, ...barProps } = props; return Bar {...barProps} />;};// wrapped internal componentexport const Foo = (props) => { return WrappedFoo {...props} />;};// explicit props objectexport const Foo = () => { const barProps = { name: 'bar', baz: 123, }; return Bar {...barProps} />;};
`

### Accessibility

- Always include an `alt` prop on tags. If the image is presentational, `alt` can be an empty string or the tag needs to have `role="presentation"`. eslint: jsx-a11y/alt-text

Bad
`tsx
img src="hello.jpg" />
`

Good
`tsx
img src="hello.jpg" alt="Me waving hello" />img src="hello.jpg" alt="" />img src="hello.jpg" role="presentation" />
`

- Don't use words like "image", "photo", or "picture" in `alt` props. eslint: jsx-a11y/img-redundant-alt

Detailed explanation
Why? Screenreaders already announce img elements as images, so there is no need to include this information in the alt text.
Bad
`tsx
img src="hello.jpg" alt="Picture of me waving hello" />
`

Good
`tsx
img src="hello.jpg" alt="Me waving hello" />
`

- Use only valid, non-abstract ARIA roles. eslint: jsx-a11y/aria-role

Bad
`tsx
div role="datepicker" />div role="range" />
`

Good
`tsx
div role="button" />
`

- Don't use `accessKey` on elements. eslint: jsx-a11y/no-access-key

Detailed explanation
Why? Inconsistencies between keyboard shortcuts and keyboard commands used by people using screenreaders and keyboards complicate accessibility.
Bad
`tsx
button accesskey="s">Click me!button>
`

Good
`tsx
button>Click me!button>
`

### JSX

- Wrap JSX tags in parentheses when they span more than one line. eslint: react/jsx-wrap-multilines

Bad
`tsx
export const Foo = () => { return Bar> Baz /> Bar>;};
`

Good
`tsx
export const Foo = () => { return ( Bar> Baz /> Bar> );};
`

- Always self-close tags that have no children. eslint: react/self-closing-comp

Bad
`tsx
Foo variant="stuff">Foo>
`

Good
`tsx
Foo variant="stuff" />
`

- If your component has multiline properties, close its tag on a new line. eslint: react/jsx-closing-bracket-location

Bad
`tsx
Foo bar="bar" baz="baz" />
`

Good
`tsx
Foo bar="bar" baz="baz"/>
`

### Files and directories

For the most part, files and directories should be named in kebab-case, with some exceptions:

- Files that contain React components, or are directly linked to react components should be named in PascalCase i.e. `FlexLayout.tsx`, `FlexLayout.test.tsx`, or `FlexLayout.stories.tsx`.

- Markdown files are usually named in SNAKE_CASE (all caps), i.e. `README.md` or `NAMING_CONVENTIONS.md`.

Applicable to individual component directories, a general directory structure like the following has proven to increase navigability. Empty directories should be omitted.

- component

- contexts - Containing react contexts.

- hooks - Containing component specific hooks.

- providers - Containing provider components.

- types - Containing general type information (component props should be located with the component).

- util - Containing further utility functions.

- Component.test.tsx

- Component.tsx

- index.ts

---

## reference

`/develop/reference/`

## Reference

- 1-min read

###

#### API
Overview of all APIs across Dynatrace.Explanation

#### JavaScript runtime
Reference of available JavaScript objects, WebAPIs, and packages of the SDK for TypeScript to write app functionsReference

#### Metric units
Reference for metric units in Dynatrace AppsReference

#### React style guide
Best practices for styling your React codeReference

---

## ui-components

`/develop/ui-components/`

- Strato UI shortcuts

## Shortcuts to Strato UI components
Use the links on this page to quickly access the essential Strato Design System component libraries, design tokens, icons, and related resources for building Dynatrace App UIs.

### Strato Design System

###

#### Components
Build exceptional apps with these reusable React UI components from the Strato Design System.

#### Data visualizations
Strato data tables and charts for all kinds of data visualization.

### More resources

###

#### About Strato Design System
Get started designing and developing with Strato, the Dynatrace design system.

#### Design tokens
Look up the default values for any design token in the Strato Design System.

#### Strato versioning and releases
Learn about the versioning, release cadence, lifecycle states, and maintenance of the Strato Design System.

#### Icons
Discover Strato's libraries of icons to represent ideas, actions, and objects.
