from sqlalchemy import Column,String,JSON,Integer
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class Vehicle(BaseMixin,Base):
    detrack_id = Column(String, nullable=False)
    vehicle_name_no = Column(String, nullable=False)
    speed_limit = Column(Integer)
    stationary_limit = Column(Integer)
    mobile_no = Column(String)
    groups = Column(JSON)
    zones = Column(String)
    vehicle_types = Column(String)
    jobs = relationship("Job", back_populates="assign_to")
