from sqlalchemy import Column,String
from infrastructure.base_class import Base

class DetrackId(Base):
    detrack_id = Column(String,nullable=False)
