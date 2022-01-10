from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.job import Job
from core.entity.job import Job as JobDTO

class JobRepositiory(BaseRepo):
    def persist(self,job) -> JobDTO:
        new_job = Job(**job.dict())
        new_job = self.create(new_job)
        return JobDTO.from_orm(new_job)
    
    def update(self,id,job) -> JobDTO:
        job_orm = self.read(Job,id)
        updated_job = super().update(job_orm,job.dict())
        return JobDTO.from_orm(updated_job)
        
    def list(self) -> List[JobDTO]:
        jobs = self.readAll(Job)
        return [JobDTO.from_orm(Job) for job in jobs]
    
    def delete(self,job) -> None:
        job_orm = self.read(Job,job.id)
        super().delete(job_orm)
        
    def getById(self,id) -> JobDTO:
        job_orm = self.read(Job,id)
        return JobDTO.from_orm(job_orm)