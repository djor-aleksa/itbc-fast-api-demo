from beverages.models.schemas import BeverageSchema, BeverageSchemaIn, BeverageSchemaUpdate
from beverages.controllers import BeveragesController
from init_app import app
from fastapi import HTTPException


@app.get("/api/beverages", response_model=list[BeverageSchema])
def get_all_beverages():
    return BeveragesController.get_all_beverages()


@app.get("/api/beverages/id/{beverage_id}", response_model=BeverageSchema)
def get_beverage_by_id(beverage_id: int):
    return BeveragesController.get_beverage_by_id(beverage_id)


@app.get("/api/beverages/name", response_model=BeverageSchema)
def find_beverage_by_name(name: str = None):
    if name is None:
        return HTTPException(status_code=400, detail="No name to look for is provided")
    response = BeveragesController.find_beverage_by_name(name)
    return response


@app.post("/api/beverages", response_model=BeverageSchema)
def create(beverage: BeverageSchemaIn):
    response = BeveragesController.create(**beverage.__dict__)
    return response


@app.put("/api/beverages/{id}", response_model=BeverageSchema)
def update(beverage_id: int, update_data: BeverageSchemaUpdate):
    return BeveragesController.update_beverage(update_data.__dict__, beverage_id)


@app.delete("/api/beverages/{beverage_id}")
def delete(beverage_id: int):
    try:
        BeveragesController.delete_beverage(beverage_id)
        return {"message": "Beverage successfully deleted."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
