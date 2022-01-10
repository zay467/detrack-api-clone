from typing import Collection
from sqlalchemy import Column,String,Date, Float,Enum
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
import enum

class job_type_enum(str,enum.Enum):
    delivery = "Delivery"
    collection = "Collection" 

class Job(BaseMixin,Base):
    date = Column(Date)
    type = Column(Enum(job_type_enum))
    address = Column(String)
    deliver_to_collect_from = Column(String)
    phone = Column(String)
    email = Column(String)
    assign_to = Column(String)
    instructions = Column(String)
    received_by_sent_by = Column(String)
    do = Column(String)
    status = Column(String)
    time = Column(String)
    pod_lat = Column(Float)
    pod_lng = Column(Float)
    job_price = Column(String)
    total_price = Column(String)
    priority = Column(String)
    address_lat = Column(Float)
    address_lng = Column(Float)
    items = relationship("JobItem", back_populates="job")
