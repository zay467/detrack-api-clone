from typing import List
from core.entity.job import Job
from core.entity.job_item import JobItem
from infrastructure.repository.job import JobRepositiory
from decorators.dependent_repos import DependentRepos

dependent_repos = {
    'job_repo': JobRepositiory,
}

@DependentRepos(dependencies=dependent_repos)
class JobService:
    def getAllJob(self) -> List[Job]:
        return self.job_repo.list()
    
    def createJob(self,job) -> Job:
        new_job = self.job_repo.persist(job)
        for item in job.items:
            self.job_repo.persistJobItem(new_job.id,item)
        job = self.job_repo.getById(new_job.id)
        return job
    
    def updateJob(self,id,job) -> Job:
        return self.job_repo.update(id,job)
    
    def deleteJob(self,id) -> None:
        self.job_repo.delete(id)
        return

    def getJobByID(self,id) -> Job:
        return self.job_repo.getById(id)

    def createJobItem(self,job_id,job_item) -> None:
        self.job_repo.persistJobItem(job_id,job_item)
        return 

    def updateJobItem(self,job_item_id,job_item) -> None:
        self.job_repo.updateJobItem(job_item_id,job_item)
        return 

    def deleteJobItem(self,job_item_id) -> None:
        self.job_repo.deleteJobItem(job_item_id)
        return 