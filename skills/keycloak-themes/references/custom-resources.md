# Custom Resources — CSS, JS, Images, Footer

Source: https://www.keycloak.org/ui-customization/themes

## Stylesheets

1. Create `themes/<name>/<type>/resources/css/<file>.css`
2. Add to `styles` in `theme.properties`

```css
/* themes/mytheme/login/resources/css/styles.css */
.login-pf body {
    background: DimGrey none;
}
```

```properties
# theme.properties — custom only (drops parent styles):
styles=css/styles.css

# theme.properties — extend parent, override last:
styles=css/login.css css/styles.css
```

Your stylesheet must be **listed last** to override parent rules.

## Scripts

1. Create `themes/<name>/<type>/resources/js/<file>.js`
2. Add to `scripts` in `theme.properties`

```javascript
// themes/mytheme/login/resources/js/script.js
alert('Hello');
```

```properties
scripts=js/script.js
```

## Images (web pages)

Place in `themes/<name>/<type>/resources/img/`.

**In CSS:**

```css
body {
    background-image: url('../img/image.jpg');
    background-size: cover;
}
```

**In Freemarker templates:**

```html
<img src="${url.resourcesPath}/img/image.jpg" alt="My image description">
```

## Images (email theme)

Place in `themes/<name>/email/resources/img/`.

```html
<img src="${url.resourcesUrl}/img/logo.jpg" alt="My logo">
```

Common resources (absolute URL required for email clients):

```html
<img src="${url.resourcesCommonUrl}/img/logo.png" alt="My logo">
```

Use `*Url` variants, not `*Path` — email clients cannot resolve relative paths.

## Custom login footer

Create `themes/<name>/login/footer.ftl`:

```html
<#macro content>
<#-- footer at the end of the login box -->
<div>
    <ul id="kc-login-footer-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</div>
</#macro>
```

## Identity provider icons

In `themes/<name>/login/theme.properties`:

```properties
kcLogoIdP-myProvider = fa fa-lock
```

Where `myProvider` is the IdP alias. Use PatternFly 4 / Font Awesome icon classes.
See `themes/keycloak/login/theme.properties` in bundled JAR for social provider examples.

## Dev workflow

Run with cache disabled to edit files in `themes/` without restart:

```bash
bin/kc.sh start \
  --spi-theme--static-max-age=-1 \
  --spi-theme--cache-themes=false \
  --spi-theme--cache-templates=false
```

Clear gzip cache if needed: `rm -rf data/tmp/kc-gzip-cache`
