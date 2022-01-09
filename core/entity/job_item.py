from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import uuid

from sqlalchemy.orm import relationship


class JobItem(BaseModel):
    sku :Optional[str]
    description:Optional[str]
    purchase_order_number:Optional[str]
    batch_number:Optional[str]
    expiry_date:Optional[str]
    comments:Optional[str]
    quantity:Optional[int]
    unit_of_measure:Optional[str]
    checked:Optional[bool]
    actual_quantity:Optional[int]
    inbound_quantity:Optional[int]
    unload_time_estimate:Optional[str]
    unload_time_actual:Optional[str]
    follow_up_quantity:Optional[int]
    follow_up_reason:Optional[str]
    rework_quantity:Optional[int]
    rework_reason:Optional[str]
    reject_quantity:Optional[int]
    reject_reason:Optional[str]
    weight:Optional[float]
    serial_numbers:Optional[List[str]]
    class Config():
        orm_mode = True
    