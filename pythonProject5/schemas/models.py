from pydantic import BaseModel

class Item(BaseModel):
    item_id : int
    name: str
    quantity: int
    cost: int
    tax_price: float


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str
