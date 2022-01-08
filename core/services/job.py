from typing import List
from core.entity.job import Job
from infrastructure.repository.job import JobRepositiory
from decorators.dependent_repos import DependentRepos

dependent_repos = {
    'job_repo': JobRepositiory
}

@DependentRepos(dependencies=dependent_repos)
class JobService:
    def getAllJob(self) -> List[Job]:
        return self.job_repo.list()
    
    def addJob(self,job) -> Job:
        new_job = self.job_repo.persist(job)
        return new_job
    
    def updateJob(self,id:int,job) -> Job:
        self.detrack_id_repo.readByDetrackId(job.detrack_id)
        return self.job_repo.update(id,job)
    
    def deleteJob(self,id:int) -> None:
        job = self.job_repo.getById(id)
        self.job_repo.delete(job)