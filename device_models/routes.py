from fastapi import HTTPException

from device_models.controllers.device_model_controller import DeviceModelsController
from device_models.models.schemas import DeviceModelSchema, DeviceModelSchemaIn, DeviceModelSchemaUpdate
from init_app import app


@app.get("/api/device-models", response_model=list[DeviceModelSchema])
def get_all_device_models():
    return DeviceModelsController.get_all_device_models()


@app.get("/api/device-models/{device_model_id}", response_model=DeviceModelSchema)
def get_device_model_by_id(device_model_id: int):
    return DeviceModelsController.get_device_model_by_id(device_model_id)


@app.post("/api/device-models", response_model=DeviceModelSchema)
def create_device_model(device_model: DeviceModelSchemaIn):
    response = DeviceModelsController.create_device_model(**device_model.__dict__)
    return response


@app.put("/api/device-models/{id}", response_model=DeviceModelSchema)
def update_device_model(beverage_id: int, update_data: DeviceModelSchemaUpdate):
    return DeviceModelsController.update_device_model(update_data.__dict__, beverage_id)


@app.delete("/api/device-models/{device_model_is}")
def delete_device_model(device_model_id: int):
    try:
        DeviceModelsController.delete_device_model(device_model_id)
        return {"message": "Device model successfully deleted."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))