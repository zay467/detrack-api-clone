from typing import List
from core.entity.job_item import JobItem
from infrastructure.repository.detrack_id import DetrackIdRepository
from infrastructure.repository.job_item import JobItemRepositiory
from decorators.dependent_repos import DependentRepos
import json

dependent_repos = {
    'detrack_id_repo': DetrackIdRepository,
    'job_item_repo': JobItemRepositiory
}

@DependentRepos(dependencies=dependent_repos)
class JobService:
    def getAllJobItem(self) -> List[JobItem]:
        return self.job_item_repo.list()
    
    def addJobItem(self,job_item) -> JobItem:
        self.detrack_id_repo.readByDetrackId(job_item.detrack_id)
        new_job_item = self.job_item_repo.persist(job_item)
        return new_job_item
    
    def updateJobItem(self,id:int,job_item) -> JobItem:
        self.detrack_id_repo.readByDetrackId(job_item.detrack_id)
        return self.job_item_repo.update(id,job_item)
    
    def deleteJobItem(self,id:int) -> None:
        job_item = self.job_item_repo.getById(id)
        self.job_item_repo.delete(job_item)