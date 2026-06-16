# Overview — Theme Types & Configuration

Source: https://www.keycloak.org/ui-customization/themes

## What themes customize

Keycloak provides theme support for web pages and emails, allowing integration
with application branding.

## Theme types

| Type | Customizes |
|------|------------|
| Account | Account Console |
| Admin | Admin Console |
| Email | Transactional emails |
| Login | Login forms |
| Welcome | Welcome page |

A single theme directory can provide multiple types (e.g. `login` + `email`).

## Configuring via Admin Console

All types **except Welcome** are set in Admin Console:

1. Log into Admin Console
2. Select realm (top-left dropdown)
3. **Realm Settings** → **Themes** tab
4. Select theme per type → **Save**
5. Refresh Admin Console page to see admin theme changes

**Master Admin Console:** set Admin Console theme on the `master` realm.

**Per-client login theme:** clients can override the realm login theme.

## Welcome theme

Configured via server startup option (not Admin Console):

```bash
bin/kc.sh start --spi-theme--welcome-theme=custom-theme
```

## Default bundled themes

Shipped in `keycloak-themes-{version}.jar` inside the server distribution
(`$KEYCLOAK_HOME/lib/lib/main/org.keycloak.keycloak-themes-*.jar`).

The server root `themes/` directory is empty by default (contains README only).

**Do not edit bundled themes directly** — create a custom theme extending them
to simplify upgrades.

## Theme composition

A theme consists of:

- HTML templates (Apache Freemarker `.ftl`)
- Images
- Message bundles (`messages/messages_<locale>.properties`)
- Stylesheets
- Scripts
- `theme.properties` configuration

## Extending vs replacing

- **Extend** (`parent=` in `theme.properties`) — override individual resources
- **Replace everything** — only if implementing full admin/account console from
  `base` (must write `index.ftl` from scratch)

When overriding HTML templates, plan to update custom templates on Keycloak upgrades.

## Additional resources

- Default themes: inspect `keycloak-themes-*.jar`
- Examples: [keycloak-quickstarts/extension](https://github.com/keycloak/keycloak-quickstarts)
