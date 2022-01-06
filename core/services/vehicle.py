from typing import List
from core.entity.vehicle import Vehicle 
from infrastructure.repository.detrack_id import DetrackIdRepository
from infrastructure.repository.vehicle import VehicleRepositiory
from decorators.dependent_repos import DependentRepos
import json

dependent_repos = {
    'detrack_id_repo': DetrackIdRepository,
    'vehicle_repo': VehicleRepositiory
}

@DependentRepos(dependencies=dependent_repos)
class VehicleService:
    def getAllVehicle(self) -> List[Vehicle]:
        return self.vehicle_repo.list()
    
    def addVehicle(self,vehicle) -> Vehicle:
        self.detrack_id_repo.readByDetrackId(vehicle.detrack_id)
        new_vehicle = self.vehicle_repo.persist(vehicle)
        return new_vehicle
    
    def updateVehicle(self,id:int,vehicle) -> Vehicle:
        self.detrack_id_repo.readByDetrackId(vehicle.detrack_id)
        return self.vehicle_repo.update(id,vehicle)
    
    def deleteVehicle(self,id:int) -> None:
        vehicle = self.vehicle_repo.getById(id)
        self.vehicle_repo.delete(vehicle)