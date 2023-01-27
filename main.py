from starlette.responses import RedirectResponse
import uvicorn

from beverages.routes import beverage_model_router
from device_models import device_model_router
from init_app import app


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    app.include_router(device_model_router)
    app.include_router(beverage_model_router)
    uvicorn.run(app)
