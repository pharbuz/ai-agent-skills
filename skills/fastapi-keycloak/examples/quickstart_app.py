"""Quickstart example from fastapi-keycloak documentation.

Pair with references/docker-compose.yaml and realm-export.json from upstream:
https://github.com/fastapi-keycloak/fastapi-keycloak/tree/main/documentation/docs/examples/quickstart
"""

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi_keycloak import FastAPIKeycloak, OIDCUser

app = FastAPI()
idp = FastAPIKeycloak(
    server_url="http://localhost:8085/auth",
    client_id="test-client",
    client_secret="GzgACcJzhzQ4j8kWhmhazt7WSdxDVUyE",
    admin_client_secret="BIcczGsZ6I8W5zf0rZg5qSexlloQLPKB",
    realm="Test",
    callback_uri="http://localhost:8081/callback",
)
idp.add_swagger_config(app)


@app.get("/")
def root():
    return "Hello World"


@app.get("/user")
def current_users(user: OIDCUser = Depends(idp.get_current_user())):
    return user


@app.get("/admin")
def company_admin(user: OIDCUser = Depends(idp.get_current_user(required_roles=["admin"]))):
    return f"Hi admin {user}"


@app.get("/login")
def login_redirect():
    return RedirectResponse(idp.login_uri)


@app.get("/callback")
def callback(session_state: str, code: str):
    return idp.exchange_authorization_code(session_state=session_state, code=code)


if __name__ == "__main__":
    uvicorn.run("quickstart_app:app", host="127.0.0.1", port=8081)
