# Develop (platform & SDKs) — overview & map

This skill covers the **design system** (components, tokens, charts, icons) in
depth. The **develop** side — app functions, SDKs, platform services — is mapped
here with links into the live docs at <https://developer.dynatrace.com/develop/>.
Fetch the specific page when you need the exact API; these areas change faster
than the component library.

> Want this section scraped into full reference files like the components are?
> It's ~160 pages — ask and it can be added to the skill.

## App development model

Dynatrace apps run on the **Dynatrace Platform** (App Engine / AppToolkit). You
scaffold, run, and ship with the **`dt-app`** CLI:

```bash
npx dt-app create     # scaffold a new app
npx dt-app dev        # local dev server
npx dt-app build      # production build
npx dt-app deploy     # deploy to your environment
npx dt-app update     # update all @dynatrace/strato-* packages
```

Guides: <https://developer.dynatrace.com/develop/> (app-functions, data,
deploy-your-app, code-optimization, dynatrace-intelligence, navigation, …).

## SDKs (`@dynatrace-sdk/*`)

The platform SDKs are published under the `@dynatrace-sdk/` npm scope. Highlights:

| Area | SDK / module | Use for |
|------|--------------|---------|
| App runtime | `app-environment`, `app-utils`, `units`, `navigation`, `user-preferences` | environment info, app utilities, unit formatting, in-app navigation |
| React | `react-hooks` | hooks for platform data & state in React apps |
| Query | `client-query` | run DQL / Grail queries from an app |
| Documents | `client-document` | store/read app documents |
| Automation | `client-automation`, `automation-utils` | workflows & automation |
| Settings | `client-app-settings`, `client-app-settings-v2`, `client-state` | app settings & state |
| IAM | `client-iam` | identity & access |
| Notifications | `client-notification`, `client-notification-v2` | send notifications |
| Buckets / storage | `client-bucket-management`, `client-resource-store` | data retention & resources |
| Classic env | `client-classic-environment-v1`/`v2` | call classic Dynatrace APIs |
| Other | `client-hub`, `client-davis-analyzers`, `client-filter-segment-management`, `client-platform-management-service`, `client-app-engine-registry`, `client-app-engine-edge-connect` | hub, Davis AI, segments, platform mgmt, edge connect |

SDK reference: <https://developer.dynatrace.com/develop/sdks/>.

## Platform services

Core concepts and the catalog of platform services:
<https://developer.dynatrace.com/develop/platform-services/> (core-concepts,
services).

## Reference

- **APIs**: <https://developer.dynatrace.com/develop/reference/apis/>
- **JavaScript runtime**: <https://developer.dynatrace.com/develop/reference/javascript-runtime/>
- **React style guide**: <https://developer.dynatrace.com/develop/reference/react-style-guide/>
- **Metric units**: <https://developer.dynatrace.com/develop/reference/metric-units/>

## Extensions & testing

- **Extensions**: <https://developer.dynatrace.com/extend/> and the develop
  extensions guides — build Dynatrace Extensions (EF 2.0).
- **Test & troubleshoot**: <https://developer.dynatrace.com/develop/test-and-troubleshoot/>
  — testing apps and debugging common issues.

## Quickstart & release notes

- Quickstart: <https://developer.dynatrace.com/quickstart/>
- Release notes: <https://developer.dynatrace.com/release-notes/>
