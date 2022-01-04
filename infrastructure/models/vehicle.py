from sqlalchemy import Column,String
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base
from sqlalchemy.orm import relationship

class Vehicle(BaseMixin,Base):
    detrack_id = Column(String, nullable=False)
    vehicle_name_no = Column(String)
    speed_limit = Column(String)
    stationary_limit = Column(String)
    mobile_no = Column(String)
    groups = Column(String)
    zones = Column(String)
    vehicle_types = Column(String)
