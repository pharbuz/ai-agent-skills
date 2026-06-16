---
name: keycloak-themes
description: >-
  Create, customize, and deploy Keycloak themes for login, account, admin, email,
  and welcome pages. Trigger WHENEVER the user works on Keycloak UI customization,
  theme.properties, Freemarker .ftl templates, login theme CSS/JS, email message
  bundles, META-INF/keycloak-themes.json, themes/ directory layout, realm theme
  settings, dark mode, or Theme Selector / Theme Resource / Locale Selector SPIs.
  Covers extending parent themes, dev cache flags, JAR deployment to providers/,
  and PatternFly-based styling.
---

# keycloak-themes — Keycloak UI customization

Keycloak themes customize end-user facing web pages and emails. Extend bundled
themes rather than editing `keycloak-themes-*.jar` directly.

[Official docs]: https://www.keycloak.org/ui-customization/themes

## Theme types

| Type | Purpose | Configured via |
|------|---------|----------------|
| `login` | Login forms | Admin Console → Realm Settings → Themes |
| `account` | Account Console | same |
| `admin` | Admin Console | same (`master` realm for master admin UI) |
| `email` | Transactional emails | same |
| `welcome` | Welcome page | CLI: `--spi-theme--welcome-theme=<name>` |

Clients can override the **login** theme per client.

## Directory layout

```
themes/
└── mytheme/
    ├── login/
    │   ├── theme.properties
    │   ├── login.ftl              # optional overrides
    │   ├── footer.ftl
    │   ├── messages/messages_en.properties
    │   └── resources/
    │       ├── css/styles.css
    │       ├── js/script.js
    │       └── img/logo.png
    └── email/
        ├── theme.properties
        └── messages/messages_en.properties
```

Theme name = directory name under `themes/`. Each type is a subdirectory with
its own `theme.properties`.

## Quick start

### 1. Dev mode (disable caching)

```bash
bin/kc.sh start \
  --spi-theme--static-max-age=-1 \
  --spi-theme--cache-themes=false \
  --spi-theme--cache-templates=false
```

Re-enable caching in production. Clear cache manually: delete `data/tmp/kc-gzip-cache`.

### 2. Minimal login theme

`themes/mytheme/login/theme.properties`:

```properties
parent=base
import=common/keycloak
```

Or `parent=keycloak` for the full Keycloak look. Set **Login Theme** to
`mytheme` in Realm Settings → Themes.

### 3. Add custom CSS

`themes/mytheme/login/resources/css/styles.css`:

```css
.login-pf body { background: DimGrey none; }
```

`theme.properties`:

```properties
parent=keycloak
import=common/keycloak
styles=css/login.css css/styles.css
```

List parent styles first; **your stylesheet last** to override.

## theme.properties

Key keys: `parent`, `import`, `styles`, `scripts`, `locales`, `abstract`.
Env substitution: `${env.VAR:default}`, `${java.version}`.

Full reference → [`references/theme-properties.md`](references/theme-properties.md).

## Templates & emails

Prefer **CSS over `.ftl` overrides**. Copy from `theme/base/<type>/` in bundled
JAR only when needed. Admin/account use single `index.ftl`.

Emails: `themes/mytheme/email/messages/messages_en.properties` with
`*Subject`, `*Body`, `*BodyHtml` keys per email type.

Emails need absolute image URLs (`${url.resourcesUrl}`, not `*Path`).

Detail → [`references/templates-and-emails.md`](references/templates-and-emails.md),
[`references/custom-resources.md`](references/custom-resources.md).

## Production deployment

JAR → `providers/` + `META-INF/keycloak-themes.json` listing theme name and types.
JAR paths: `theme/mytheme/login/...` (not `themes/`).

Detail → [`references/deploying.md`](references/deploying.md).

## Common pitfalls

- Edit bundled JAR themes → breaks upgrades; use `parent=`
- `styles=css/styles.css` alone drops parent CSS — list `css/login.css` first
- Email images need `${url.resourcesUrl}` (absolute URLs)
- Welcome theme: CLI only (`--spi-theme--welcome-theme`), not Admin Console
- Dark mode / SPIs → [`references/theme-spis.md`](references/theme-spis.md)

## Reference files

| File | Covers |
|------|--------|
| `references/overview.md` | Types, admin config, default themes |
| `references/theme-properties.md` | All theme.properties keys, CSS class props |
| `references/custom-resources.md` | CSS, JS, images, footer, IdP icons |
| `references/templates-and-emails.md` | FTL overrides, message bundles |
| `references/deploying.md` | JAR structure, keycloak-themes.json, providers/ |
| `references/theme-spis.md` | Theme Selector, Theme Resource, Locale Selector SPIs |
