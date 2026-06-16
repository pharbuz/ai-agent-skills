# Freemarker Templates & Emails

Source: https://www.keycloak.org/ui-customization/themes

## When to override templates

Keycloak uses [Apache Freemarker](https://freemarker.apache.org/) for HTML.

**Prefer CSS customization** over template overrides because:

- Upgrades may require merging changes into custom templates
- CSS adapts UI without forking page structure
- User Profile handles custom attributes without template changes

Override `.ftl` files only when CSS/message bundles are insufficient.

## Overriding templates

1. Find template in `theme/base/<type>/` inside `keycloak-themes-*.jar`
2. Copy to `themes/<mytheme>/<type>/<template>.ftl`
3. Edit and back up — diff against new base templates on upgrades

Admin and account consoles use a single `index.ftl` for the SPA shell.

## Login template example

Copy `themes/base/login/login.ftl` → `themes/mytheme/login/login.ftl`:

```html
<#import "template.ftl" as layout>
<h1>HELLO WORLD!</h1>
...
```

## Email message bundles

Add `themes/<mytheme>/email/messages/messages_en.properties`.

Three keys per email type:

| Suffix | Purpose |
|--------|---------|
| `*Subject` | Email subject line |
| `*Body` | Plain text body (`{0}` = link placeholder) |
| `*BodyHtml` | HTML body |

Example — password reset:

```properties
passwordResetSubject=My password recovery
passwordResetBody=Reset password link: {0}
passwordResetBodyHtml=<a href="{0}">Reset password</a>
```

Full list of email keys: `themes/base/email/messages/messages_en.properties`
in bundled JAR.

## Locale files

Naming: `messages_<locale>.properties` (e.g. `messages_de.properties`).

Declare supported locales in `theme.properties`:

```properties
locales=en,de,pl
```

## Freemarker resources

- [FreeMarker Manual](https://freemarker.apache.org/docs/index.html)
- User Profile rendering: Keycloak Server Admin docs → User Profile
