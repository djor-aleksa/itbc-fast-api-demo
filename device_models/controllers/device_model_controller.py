from device_models.services import DeviceModelsService
from device_models.models.schemas import DeviceModelSchema


class DeviceModelsController:

    @staticmethod
    def get_all_device_models():
        all_device_models = DeviceModelsService.get_all_device_models()
        all_device_schemas = []
        for device in all_device_models:
            all_device_schemas.append(DeviceModelSchema(**device.__dict__))
        return all_device_schemas

    @staticmethod
    def get_device_model_by_id(device_model_id: int):
        return DeviceModelsService.get_device_model_by_id(device_model_id)

    @staticmethod
    def create_device_model(model_name: str, model_number: str, water_capacity_liters: float,
                            coffee_capacity_kgs: float, milk_capacity_kgs: float, sugar_capacity_kgs: float,
                            sweetener_capacity_count: int, cups_capacity_count: int):

        return DeviceModelsService.create_device_model(model_name, model_number, water_capacity_liters,
                                                       coffee_capacity_kgs, milk_capacity_kgs, sugar_capacity_kgs,
                                                       sweetener_capacity_count, cups_capacity_count)

    @staticmethod
    def delete_device_model(device_model_id: int):
        try:
            DeviceModelsService.delete_device_model(device_model_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_device_model(attributes_dict: dict, device_model_id: int):
        return DeviceModelsService.update_device_model(attributes_dict, device_model_id)
