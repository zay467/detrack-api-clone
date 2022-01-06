from typing import List, Optional
from pydantic import BaseModel,Json

class Vehicle(BaseModel):
    detrack_id: str 
    vehicle_name_no: str 
    speed_limit: Optional[int]
    stationary_limit: Optional[int]
    mobile_no: Optional[str]
    groups: Optional[List[str]]
    zones: Optional[str]
    vehicle_types: Optional[str]