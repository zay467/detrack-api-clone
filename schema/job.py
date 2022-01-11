from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from .job_item import JobItem
from infrastructure.models.job import job_type_enum

class Job(BaseModel):
    date : date
    type : job_type_enum
    address : str
    deliver_to_collect_from : Optional[str]
    phone : Optional[str]
    email : Optional[str]
    assign_to : Optional[str]
    instructions : Optional[str]
    received_by_sent_by : Optional[str]
    do : str
    pod_lat : Optional[float]
    pod_lng : Optional[float]
    job_price : Optional[str]
    total_price : Optional[str]
    priority : Optional[int]
    address_lat : Optional[float]
    address_lng : Optional[float]
    items : Optional[List[JobItem]]
  