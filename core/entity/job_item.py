from typing import  Optional
from pydantic import BaseModel
from datetime import datetime
import uuid

class JobItem(BaseModel):
    id : uuid.UUID
    sku : str
    description : str
    quantity : int
    reject : int
    reason : str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[uuid.UUID] = None
    updated_user_id: Optional[uuid.UUID] = None
    class Config():
        orm_mode = True
    