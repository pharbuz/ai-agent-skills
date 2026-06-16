# theme.properties Reference

Source: https://www.keycloak.org/ui-customization/themes

Set in `themes/<theme-name>/<type>/theme.properties`.

## Core properties

| Property | Description |
|----------|-------------|
| `parent` | Parent theme to extend (`base`, `keycloak`, custom) |
| `import` | Import resources from another theme (e.g. `common/keycloak`) |
| `abstract` | If `true`, theme is base-only — hidden from realm theme picker |
| `common` | Override common resource path; default `common/keycloak` |
| `styles` | Space-separated CSS files relative to `resources/css/` |
| `scripts` | Space-separated JS files relative to `resources/js/` |
| `locales` | Comma-separated supported locales |
| `contentHashPattern` | Regex for hashed filenames (JS bundling) |

## URL variables in templates

`common` affects Freemarker variables:

| Variable | Returns |
|----------|---------|
| `${url.resourcesCommonPath}` | Path only (web pages) |
| `${url.resourcesCommonUrl}` | Full URL with scheme/host (emails) |
| `${url.resourcesPath}` | Theme-specific path |
| `${url.resourcesUrl}` | Theme-specific full URL |

## CSS class properties

Keycloak themes expose properties to change CSS classes for UI elements.
Full list: inspect `themes/keycloak/<type>/theme.properties` inside the
bundled JAR.

## Identity provider icons

Pattern: `kcLogoIdP-<alias> = <icon-class>`

```properties
kcLogoIdP-myProvider = fa fa-lock
```

Social provider icons defined in `themes/keycloak/login/theme.properties`.
Icons: [PatternFly 4 icons](https://www.patternfly.org/v4/).

## Custom properties

Add arbitrary keys and reference from custom `.ftl` templates.

### System property substitution

```properties
javaVersion=${java.version}
```

### Environment variable substitution

```properties
unixHome=${env.HOME:Unix home not found}
windowsHome=${env.HOMEPATH:Windows home not found}
```

Formats:

- `${some.system.property}` — JVM system property
- `${env.ENV_VAR}` — environment variable
- `${foo\:defaultValue}` — with default if missing

If no default and no matching property/env var, the literal `${...}` remains in output.

## Example: minimal login theme

```properties
parent=base
import=common/keycloak
```

## Example: styled login theme

```properties
parent=keycloak
import=common/keycloak
styles=css/login.css css/styles.css
scripts=js/script.js
locales=en,de
```
