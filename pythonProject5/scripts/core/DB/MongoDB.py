from pydantic import BaseModel
from pymongo import MongoClient
from main import app_main
from schemas.models import Item

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
inventory = db.Shangeetha


class Item_handler:
    def welcome(self):
        return {"Welcome to Inventory"}
    def get_all(items_list):
        items = (items_list.find())
        new_item = []
        for new_item in items:
            del items["_id"]
            new_item.append(items)
            return new_item


    def create_item(item_id: int, item: Item):
        db[item_id] = (item.dict())
        inventory.insert_one(item.dict())
        return db


    def update_item(name: str, upd: Item):
        inventory.update_one({"name": name}, {"$set": upd.dict()})
        return "updated"
    def delete_item(item_id: int):
        inventory.delete_one({"items_id": item_id})
        return {
        "db": db
        }


item_object = Item_handler()
