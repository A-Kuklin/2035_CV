from fastapi import FastAPI
from fastapi.openapi.models import Info
from fastapi.openapi.utils import get_openapi


def get_custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="2035_API",
        version="1.0",
        description="2035_API",
        routes=app.routes,
    )
    openapi_schema["info"] = Info(title="2035_API", version="1.0")
    app.openapi_schema = openapi_schema
    return app.openapi_schema
