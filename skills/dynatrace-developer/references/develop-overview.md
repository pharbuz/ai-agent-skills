# Develop (platform, SDKs, guides) — index

The **develop** side of developer.dynatrace.com — how to build, wire up data,
deploy, and test Dynatrace Platform apps — is captured in full in the
`develop-*.md` reference files below. This page is the map; open the specific
file for the scraped page content.

| Area | Reference file | Covers |
|------|----------------|--------|
| Guides | [`develop-guides.md`](develop-guides.md) | app functions, data access/ingest/storage, navigation & intents, workflows, security, privacy, visualizing data, code optimization, keyboard shortcuts, deploy (53 pages) |
| SDKs | [`develop-sdks.md`](develop-sdks.md) | every `@dynatrace-sdk/*` module (overview + latest version): query, document, automation, IAM, settings, state, notifications, app-environment, react-hooks, … |
| Platform services | [`develop-platform-services.md`](develop-platform-services.md) | core concepts (auth, versions, error handling, filtering, locking) + each service (Grail, automation, documents, settings, notifications, …) |
| Reference | [`develop-reference.md`](develop-reference.md) | APIs (classic/latest), JavaScript runtime, metric units, React style guide, automation-action React components |
| Extensions | [`develop-extensions.md`](develop-extensions.md) | Extensions 2.0 + the Dynatrace Extensions VS Code add-on |
| Test & troubleshoot | [`develop-test-troubleshoot.md`](develop-test-troubleshoot.md) | unit/E2E testing, debugging apps & app functions, connectivity |

Live docs: <https://developer.dynatrace.com/develop/>.

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

## SDKs (`@dynatrace-sdk/*`) — quick map

The platform SDKs are published under the `@dynatrace-sdk/` npm scope. Full,
scraped detail is in [`develop-sdks.md`](develop-sdks.md); this is the at-a-glance index:

| Area | SDK / module | Use for |
|------|--------------|---------|
| App runtime | `app-environment`, `app-utils`, `units`, `navigation`, `user-preferences` | environment info, app utilities, unit formatting, in-app navigation |
| React | `react-hooks` | hooks for platform data & state in React apps |
| Query | `client-query` | run DQL / Grail queries from an app |
| Documents | `client-document` | store/read app documents |
| Automation | `client-automation`, `automation-utils` | workflows & automation |
| Settings / state | `client-app-settings`, `client-app-settings-v2`, `client-state` | app settings & state |
| IAM | `client-iam` | identity & access |
| Notifications | `client-notification`, `client-notification-v2` | send notifications |
| Buckets / storage | `client-bucket-management`, `client-resource-store` | data retention & resources |
| Classic env | `client-classic-environment-v1`/`v2` | call classic Dynatrace APIs |
| Other | `client-hub`, `client-davis-analyzers`, `client-filter-segment-management`, `client-platform-management-service`, `client-app-engine-registry`, `client-app-engine-edge-connect` | hub, Davis AI, segments, platform mgmt, edge connect |

> For calling the Dynatrace REST API from **async Python** (outside an app — e.g.
> a backend service), see the separate `dt-async` skill in this repo.

## Quickstart & release notes

- Quickstart: <https://developer.dynatrace.com/quickstart/>
- Release notes: <https://developer.dynatrace.com/release-notes/>
