from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from api.router import router
from utils.openapi import get_custom_openapi


app = FastAPI(title='2035_API')
app.include_router(router)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API Docs",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_schema():
    return get_custom_openapi(app)



