from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import uuid

from sqlalchemy.orm import relationship


class JobItem(BaseModel):
    sku :str
    description:str
    purchase_order_number:str
    batch_number:str
    expiry_date:str
    comments:str
    quantity:int
    unit_of_measure:str
    checked:bool
    actual_quantity:int
    inbound_quantity:int
    unload_time_estimate:str
    unload_time_actual:str
    follow_up_quantity:int
    follow_up_reason:str
    rework_quantity:int
    rework_reason:str
    reject_quantity:int
    reject_reason:str
    weight:float
    serial_numbers=List[str]
    class Config():
        orm_mode = True
    