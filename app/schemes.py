from pydantic import BaseModel ,Field
import uuid


class Item(BaseModel):
    unique_id: str= Field(default_factory=lambda: str(uuid.uuid4()))
    order_id: str
    pizza_type: str
    size: str
    quantity: int
    is_delivery: bool
    special_instructions:str = Field(default=None)
    status: str = Field(default="PREPARING")


