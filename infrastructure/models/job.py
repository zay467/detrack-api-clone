from sqlalchemy import Column,String,Date, Float,Enum,Integer
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from datetime import datetime 
import enum

class job_type_enum(str,enum.Enum):
    delivery = "Delivery"
    collection = "Collection" 

class job_status_enum(str,enum.Enum):
    in_progress = "In Progress"
    delivered = "Delivered"
    collected = "Collected"

class Job(BaseMixin,Base):
    date = Column(Date,nullable=False)
    type = Column(Enum(job_type_enum),nullable=False)
    address = Column(String,nullable=False)
    deliver_to_collect_from = Column(String)
    phone = Column(String)
    email = Column(String)
    assign_to = Column(String)
    instructions = Column(String)
    received_by_sent_by = Column(String)
    do = Column(String,nullable=False)
    status = Column(Enum(job_status_enum),default=job_status_enum.in_progress)
    time = Column(String,default=datetime.now().strftime("%H:%M"))
    pod_lat = Column(Float)
    pod_lng = Column(Float)
    job_price = Column(String)
    total_price = Column(String)
    priority = Column(Integer)
    address_lat = Column(Float)
    address_lng = Column(Float)
    items = relationship("JobItem", back_populates="job",passive_deletes=True)
