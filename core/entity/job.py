from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime,date
from .job_item import JobItem
from .vehicle import Vehicle
from infrastructure.models.job import job_type_enum,job_status_enum
import uuid

class Job(BaseModel):
    id : uuid.UUID
    date : date
    type : job_type_enum
    address : str
    deliver_to_collect_from : str
    phone : str
    email : str
    assign_to : Optional[Vehicle] = None
    instructions : str
    received_by_sent_by : str
    do : str
    status : job_status_enum
    time : str
    pod_lat : float
    pod_lng : float
    job_price : str
    total_price : str
    priority : int
    address_lat : float
    address_lng : float
    items : Optional[List[JobItem]] = []
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[uuid.UUID] = None
    updated_user_id: Optional[uuid.UUID] = None
    class Config():
        orm_mode = True