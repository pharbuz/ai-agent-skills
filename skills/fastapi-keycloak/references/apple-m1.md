# Apple MacBook M1 issues

On Apple Silicon, the stock Keycloak Docker image may fail to start during local
testing. Rebuild the image locally:

```shell
#!/bin/zsh

cd /tmp
git clone git@github.com:keycloak/keycloak-containers.git
cd keycloak-containers/server
git checkout 16.1.0
docker build -t "jboss/keycloak:16.1.0" .
```

Then use the rebuilt image in `docker-compose.yaml`.
