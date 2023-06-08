from fastapi import APIRouter

from schemas.models import Email, Item
from scripts.constants.app_constants import Item_ends
from scripts.core.handlers.Item_handler import read_item, get_all, create_item, update_item, delete_item, \
    pipeline_aggregate
from scripts.core.handlers.email_handler import send_email

app = APIRouter()


@app.get("/")
def fun():
    return read_item()


@app.get(Item_ends.get_items)
def fun():
    return get_all()


@app.post(Item_ends.create_items)
def fun(item: Item):
    return create_item(item)


@app.put(Item_ends.update_items)
def fun(name: str, upd: Item):
    return update_item(name, upd)


@app.delete(Item_ends.delete_items)
def fun(name: str):
    return delete_item(name)


@app.get(Item_ends.get_Total_price)
def fun():
    return pipeline_aggregate()


@app.post(Item_ends.send_email)
def fun(email: Email):
    return send_email(email)
