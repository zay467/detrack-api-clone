from infrastructure.models.detrack_id import DetrackId
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from infrastructure.session import get_db
from infrastructure.models.vehicle import Vehicle
from core.entity.detrack_id import DetrackId as DetrackIdDTO
from exceptions.http import NOT_FOUND
from core.entity.job import Job as JobDTO
from infrastructure.models.job import Job
from typing import List
from exceptions.repo import SQLALCHEMY_ERROR
from sqlalchemy.exc import SQLAlchemyError
import uuid

class CourierRepository:
    def __init__(self,db:Session=Depends(get_db)):
        self._db = db

    def persist(self,detrack_id):
        new_detrack_id = DetrackId(detrack_id=detrack_id)
        self._db.add(new_detrack_id)
        self._db.flush()
        self._db.refresh(new_detrack_id)
        return DetrackIdDTO.from_orm(new_detrack_id)

    def readByDetrackId(self,detrack_id):
        detrack_id = self._db.query(DetrackId).filter(DetrackId.detrack_id == detrack_id).first()
        if detrack_id is None:
            raise NOT_FOUND("Not a valid Detrack ID.")
        return DetrackIdDTO.from_orm(detrack_id)

    def getVehicleIdByDetrackId(self,detrack_id) -> uuid.UUID:
        vehicle_id = self._db.query(Vehicle).filter(Vehicle.detrack_id == detrack_id).first()
        if vehicle_id is None:
            raise NOT_FOUND("Not a associated Detrack ID.")
        return vehicle_id.id

    def listByAssignToIdAndTypeAndDate(self,id,type,date) -> List[JobDTO]:
        try:
            jobs = self._db.query(Job).filter(Job.assign_to_id == id,Job.type == type,Job.date == date).all()
            return [JobDTO.from_orm(job) for job in jobs]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listByAssignToIdAndType(self,id,type) -> List[JobDTO]:
        try:
            jobs = self._db.query(Job).filter(Job.assign_to_id == id,Job.type == type).all()
            return [JobDTO.from_orm(job) for job in jobs]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def updateStatus(self,id): 
        try:
            job = self._db.query(Job).filter(Job.id == id)
            if job.first() is None:
                raise NOT_FOUND("Job not found.")
            print(job.first().type)
            if job.first().type == "Delivery":
                job.update({"status":"Delivered"})
            else:
                job.update({"status":"Collected"})
            self._db.flush()
            return 
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
