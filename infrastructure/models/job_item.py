from decimal import Inexact
from sqlalchemy import Column,String,JSON,Integer,Boolean, Date, Float
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

class JobItem(BaseMixin,Base):
    sku = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    reject = Column(Integer)
    reason = Column(String)
    job_id=Column(UUID(as_uuid=True),ForeignKey("job.id"))
    job=relationship("Job",back_populates="items")


