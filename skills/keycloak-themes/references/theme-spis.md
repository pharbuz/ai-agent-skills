# Theme SPIs & Dark Mode

Source: https://www.keycloak.org/ui-customization/themes

## Dark mode

PatternFly-based themes (admin console, account console) support light/dark variants.

**Disable:** Admin Console → Realm Settings → Themes → uncheck **Dark mode** → Save.

When enabled: variant follows OS setting (light/dark) or user-agent preference.
When disabled: light variant only.

No effect on themes without light/dark support.

## Theme Selector SPI

Default: realm-configured theme is used. Clients can override login theme.

Custom logic (e.g. mobile vs desktop by User-Agent) via **Theme Selector SPI**:

Implement:

- `ThemeSelectorProviderFactory`
- `ThemeSelectorProvider`

## Theme Resource SPI

For custom providers (e.g. custom authenticators) needing extra templates/resources.

### Simple approach — JAR layout

```
my-provider.jar
└── theme-resources/
    ├── templates/
    ├── resources/
    └── messages/
```

### Flexible approach — ThemeResourceSPI

Implement:

- `ThemeResourceProviderFactory`
- `ThemeResourceProvider`

Controls exactly how templates and resources are loaded.

## Locale Selector SPI

Default: `DefaultLocaleSelectorProvider`.

- i18n disabled → English
- i18n enabled → logic in [Server Admin docs](https://www.keycloak.org/docs/latest/server_admin/#_user_locale_selection)

Custom locale resolution via **LocaleSelectorSPI**:

Implement:

- `LocaleSelectorProvider`
- `LocaleSelectorProviderFactory`

`LocaleSelectorProvider.resolveLocale(RealmModel, UserModel)` — request available
via `KeycloakSession.getContext()`.

**Example:** extend `DefaultLocaleSelectorProvider`, override
`getAcceptLanguageHeaderLocale()` to return `null` — falls back to realm default.

## SPI deployment

Custom SPI providers: [Service Provider Interfaces](https://www.keycloak.org/docs/latest/server_development/index.html#_providers)

Deploy provider JAR to `providers/`, run `kc.sh build`, restart.
