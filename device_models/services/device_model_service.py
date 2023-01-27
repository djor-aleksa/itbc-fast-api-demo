from device_models.repositories import DeviceModelsRepository
from database_connector import mydb


class DeviceModelsService:

    @staticmethod
    def get_all_device_models():
        my_cursor = mydb.cursor()
        device_models_repository = DeviceModelsRepository(my_cursor=my_cursor)
        result = device_models_repository.read_all()
        my_cursor.close()
        return result

    @staticmethod
    def get_device_model_by_id(device_model_id: int):
        my_cursor = mydb.cursor()
        device_models_repository = DeviceModelsRepository(my_cursor=my_cursor)
        result = device_models_repository.get_by_id(device_model_id)
        my_cursor.close()
        return result

    @staticmethod
    def create_device_model(model_name: str, model_number: str, water_capacity_liters: float, coffee_capacity_kgs: float,
                            milk_capacity_kgs: float, sugar_capacity_kgs: float, sweetener_capacity_count: int,
                            cups_capacity_count: int):
        my_cursor = mydb.cursor()
        device_models_repository = DeviceModelsRepository(my_cursor=my_cursor)
        result = device_models_repository.create(model_name, model_number, water_capacity_liters, coffee_capacity_kgs,
                                                 milk_capacity_kgs,
                                                 sugar_capacity_kgs, sweetener_capacity_count, cups_capacity_count)
        my_cursor.close()
        return result

    @staticmethod
    def delete_device_model(device_model_id: int):
        my_cursor = mydb.cursor()
        device_models_repository = DeviceModelsRepository(my_cursor=my_cursor)
        result = device_models_repository.delete(device_model_id)
        my_cursor.close()
        return result

    @staticmethod
    def update_device_model(attributes_dict, device_model_id):
        my_cursor = mydb.cursor()
        device_models_repository = DeviceModelsRepository(my_cursor=my_cursor)
        result = device_models_repository.update(attributes_dict, device_model_id)
        my_cursor.close()
        return result
