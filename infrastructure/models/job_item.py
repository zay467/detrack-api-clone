from sqlalchemy import Column,String,JSON,Integer,Boolean, Date, Float
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

class JobItem(BaseMixin,Base):
    sku = Column(String)
    description=Column(String)
    purchase_order_number=Column(String)
    batch_number=Column(String)
    expiry_date=Column(Date)
    comments=Column(String)
    quantity=Column(Integer)
    unit_of_measure=Column(String)
    checked=Column(Boolean)
    actual_quantity=Column(Integer)
    inbound_quantity=Column(Integer)
    unload_time_estimate=Column(String)
    unload_time_actual=Column(String)
    follow_up_quantity=Column(Integer)
    follow_up_reason=Column(String)
    rework_quantity=Column(Integer)
    rework_reason=Column(String)
    reject_quantity=Column(Integer)
    reject_reason=Column(String)
    weight=Column(Float)
    serial_numbers=Column(JSON)
    job_id=Column(UUID(as_uuid=True),ForeignKey("job.id"))
    job=relationship("Job",back_populates="items")


