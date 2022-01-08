from typing import List
import json
from infrastructure.base_repo import BaseRepo
from infrastructure.models.job_item import JobItem
from core.entity.job_item import JobItem as JobItemDTO

class JobItemRepositiory(BaseRepo):
    def persist(self,job_item) -> JobItemDTO:
        new_job_item = JobItem(**job_item.dict())
        new_job_item = self.create(new_job_item)
        return JobItemDTO.from_orm(new_job_item)
    
    def update(self,id,job_item) -> JobItemDTO:
        job_item_orm = self.read(JobItem,id)
        updated_job_item = super().update(job_item_orm,job_item.dict())
        return JobItemDTO.from_orm(updated_job_item)
        
    def list(self) -> List[JobItemDTO]:
        job_items = self.readAll(JobItem)
        # vehicle_dto_list = []
        # for vehicle in vehicles:
        #     vehicle.groups = json.loads(vehicle.groups)
        #     vehicle_dto_list.append(VehicleDTO.from_orm(vehicle))
        return [JobItemDTO.from_orm(JobItem) for job_item in job_items]
    
    def delete(self,job_item) -> None:
        job_item_orm = self.read(JobItem,job_item.id)
        super().delete(job_item_orm)
        
    def getById(self,id) -> JobItemDTO:
        job_item_orm = self.read(JobItem,id)
        return JobItemDTO.from_orm(job_item_orm)