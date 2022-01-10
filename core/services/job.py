from typing import List
from core.entity.job import Job
from infrastructure.repository.job import JobRepositiory
from infrastructure.repository.job_item import JobItemRepositiory
from decorators.dependent_repos import DependentRepos

dependent_repos = {
    'job_repo': JobRepositiory,
    'job_item_repo':JobItemRepositiory
}

@DependentRepos(dependencies=dependent_repos)
class JobService:
    def getAllJob(self) -> List[Job]:
        return self.job_repo.list()
    
    def addJob(self,job) -> Job:
        new_job = self.job_repo.persist(job)
        for item in job.items:
            item.job_id=new_job.id
            self.job_item_repo.persist(item)
        return new_job
    
    def updateJob(self,id:int,job) -> Job:
        return self.job_repo.update(id,job)
    
    def deleteJob(self,id:int) -> None:
        job = self.job_repo.getById(id)
        self.job_repo.delete(job)