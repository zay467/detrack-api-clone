from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import uuid

class Vehicle(BaseModel):
    id: uuid.UUID
    detrack_id: str 
    vehicle_name_no: str 
    speed_limit: Optional[int]
    stationary_limit: Optional[int]
    mobile_no: Optional[str]
    groups: Optional[List[str]]
    zones: Optional[str]
    vehicle_types: Optional[str]
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True