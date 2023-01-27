from fastapi import HTTPException, APIRouter

from device_models.controllers.device_model_controller import DeviceModelsController
from device_models.models.schemas import DeviceModelSchema, DeviceModelSchemaIn, DeviceModelSchemaUpdate
from http import HTTPStatus

device_model_router = APIRouter(tags=["Device Models"], prefix="/api/device-models")


@device_model_router.get("", response_model=list[DeviceModelSchema])
def get_all_device_models():
    return DeviceModelsController.get_all_device_models()


@device_model_router.get("/{device_model_id}", response_model=DeviceModelSchema)
def get_device_model_by_id(device_model_id: int):
    return DeviceModelsController.get_device_model_by_id(device_model_id)


@device_model_router.post("", response_model=DeviceModelSchema)
def create_device_model(device_model: DeviceModelSchemaIn):
    response = DeviceModelsController.create_device_model(**device_model.__dict__)
    return response


@device_model_router.put("/{id}", response_model=DeviceModelSchema)
def update_device_model(beverage_id: int, update_data: DeviceModelSchemaUpdate):
    return DeviceModelsController.update_device_model(update_data.__dict__, beverage_id)


@device_model_router.delete("/{device_model_is}")
def delete_device_model(device_model_id: int):
    try:
        DeviceModelsController.delete_device_model(device_model_id)
        return {"message": "Device model successfully deleted."}
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
