from infrastructure.models.detrack_id import DetrackId
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from infrastructure.session import get_db
from core.entity.detrack_id import DetrackId as DetrackIdDTO

class DetrackIdRepository:
    def __init__(self,db:Session=Depends(get_db)):
        self._db = db

    def persist(self,detrack_id):
        new_detrack_id = DetrackId(detrack_id=detrack_id)
        self._db.add(new_detrack_id)
        self._db.flush()
        self._db.refresh(new_detrack_id)
        return DetrackIdDTO.from_orm(new_detrack_id)
