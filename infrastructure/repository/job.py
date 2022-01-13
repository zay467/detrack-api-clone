from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.job import Job
from infrastructure.models.job_item import JobItem
from core.entity.job import Job as JobDTO
from core.entity.job_item import JobItem as JobItemDTO
from exceptions.repo import SQLALCHEMY_ERROR
from sqlalchemy.exc import SQLAlchemyError

class JobRepositiory(BaseRepo):
    def persist(self,job) -> JobDTO:
        job = job.dict(exclude={'items'})
        new_job = Job(**job)
        new_job = self.create(new_job)
        return JobDTO.from_orm(new_job)
    
    def update(self,id,job) -> JobDTO:
        job_orm = self.read(Job,id)
        updated_job = super().update(job_orm,job.dict(exclude={'items'}))
        return JobDTO.from_orm(updated_job)
        
    def list(self) -> List[JobDTO]:
        jobs = self.readAll(Job)
        return [JobDTO.from_orm(job) for job in jobs]

    def listByType(self,type) -> List[JobDTO]:
        # print(self._user)
        try:
            jobs = self._db.query(Job).filter(Job.type == type).all()
            return [JobDTO.from_orm(job) for job in jobs]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def listByTypeAndDate(self,type,date) -> List[JobDTO]:
        try:
            jobs = self._db.query(Job).filter(Job.type == type,Job.date == date).all()
            return [JobDTO.from_orm(job) for job in jobs]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
    
    def delete(self,id) -> None:
        self.read(Job,id)
        super().delete(Job,id)
        
    def getById(self,id) -> JobDTO:
        job_orm = self.read(Job,id)
        return JobDTO.from_orm(job_orm)

    def persistJobItem(self,new_job_id,job_item):
        job_item = job_item.dict()
        job_item.update({"job_id": new_job_id})
        new_job_item = JobItem(**job_item)
        new_job_item = self.create(new_job_item)
        return JobItemDTO.from_orm(new_job_item)

    def updateJobItem(self,job_item_id,job_item):
        job_item_orm = self.read(JobItem,job_item_id)
        updated_job_item = super().update(job_item_orm,job_item.dict())
        return JobItemDTO.from_orm(updated_job_item)
    
    def deleteJobItem(self,id):
        self.read(JobItem,id)
        super().delete(JobItem,id)