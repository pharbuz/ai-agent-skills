# Deploying Themes

Source: https://www.keycloak.org/ui-customization/themes

## Deployment methods

| Method | When |
|--------|------|
| Copy to `themes/` | Development — hot-edit with cache disabled |
| JAR in `providers/` | Production — versioned, cluster-friendly |

## Directory deployment (dev)

```bash
cp -r mytheme/ $KEYCLOAK_HOME/themes/mytheme/
```

Select theme in Realm Settings → Themes. No restart if theme cache is disabled.

## JAR deployment (production)

### JAR structure

```
mytheme.jar
├── META-INF/
│   └── keycloak-themes.json
└── theme/
    └── mytheme/
        ├── login/
        │   ├── theme.properties
        │   ├── login.ftl
        │   ├── resources/css/styles.css
        │   ├── resources/img/image.png
        │   └── messages/messages_en.properties
        └── email/
            └── messages/messages_en.properties
```

Note: JAR uses `theme/<name>/` prefix (not `themes/`).

### keycloak-themes.json

```json
{
  "themes": [{
    "name": "mytheme",
    "types": ["login", "email"]
  }]
}
```

One JAR can contain **multiple themes**, each with multiple types.

### Install

```bash
cp mytheme.jar $KEYCLOAK_HOME/providers/
bin/kc.sh build    # if using optimized distribution
bin/kc.sh start    # restart if already running
```

## Security warning

Themes contain FreeMarker templates executed by the Keycloak server process.
A malicious template can run arbitrary code as Keycloak.

- Install themes only from **trusted sources**
- Restrict write access to `themes/` and `providers/` to trusted operators

## Cache management

Production: keep theme caching enabled for performance.

Manual cache clear: delete `data/tmp/kc-gzip-cache` from server distribution
(useful after redeploying themes without disabling cache).
