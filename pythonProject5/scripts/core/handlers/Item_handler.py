from schemas.models import Item
from scripts.constants.app_constants import *
from utility.mong_utility import inventory


def read_item():
    return {"Welcome to Inventory"}


def get_all():
        items = list(inventory.find({}))
        new_item = []
        for each in items:
            del each["_id"]
            new_item.append(each)
        return new_item



def create_item(item: Item):
    try:
        inventory.insert_one(item.dict())
        return {"created"}
    except Exception as es:
        return {"not expected output came", str(es)}


def update_item(name: str, upd: Item):
    try:
        if list(inventory.find({"name": upd.name})) != []:
            return {'message': 'Item already present'}
        else:
            inventory.update_one({"name": name}, {"$set": upd.dict()})
            return {"message": "item update successfully"}

    except Exception as e:
        return {"message": f"error occurred while updating item: {str(e)}"}


def delete_item(name: str):
    try:
        inventory.delete_one({"name": name})
        return {"message": "Item deleted successfully"}
    except Exception as e:
        return {"message": f"Error occurred while deleting item: {str(e)}"}


def pipeline_aggregate():
    pipeline = [
        {
            '$addFields': {
                'Total_price': {
                    '$multiply': [
                        '$quantity', '$cost'
                    ]
                }
            }
        }, {
            '$group': {
                '_id': None,
                'sum_of_all_price': {
                    '$sum': '$Total_price'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = inventory.aggregate(pipeline)
    data = list(data)
    print(data)
    return {"Total_price": data[0]['sum_of_all_price']}
