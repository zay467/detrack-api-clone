from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

class JobItem(BaseMixin,Base):
    sku = Column(String,nullable=False)
    description = Column(String,nullable=False)
    quantity = Column(Integer,nullable=False)
    reject = Column(Integer)
    reason = Column(String)
    job_id=Column(UUID(as_uuid=True),ForeignKey("job.id",ondelete='CASCADE'))
    job=relationship("Job",back_populates="items")


