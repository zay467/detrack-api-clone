from typing import List
from core.entity.vehicle import Vehicle 
from infrastructure.repository.courier import CourierRepository
from infrastructure.repository.vehicle import VehicleRepositiory
from decorators.dependent_repos import DependentRepos

dependent_repos = {
    'courier_repo': CourierRepository,
    'vehicle_repo': VehicleRepositiory
}

@DependentRepos(dependencies=dependent_repos)
class VehicleService:
    def getAllVehicle(self) -> List[Vehicle]:
        return self.vehicle_repo.list()
    
    def addVehicle(self,vehicle) -> Vehicle:
        self.courier_repo.readByDetrackId(vehicle.detrack_id)
        new_vehicle = self.vehicle_repo.persist(vehicle)
        return new_vehicle
    
    def updateVehicle(self,id,vehicle) -> Vehicle:
        self.detrack_id_repo.readByDetrackId(vehicle.detrack_id)
        return self.vehicle_repo.update(id,vehicle)
    
    def deleteVehicle(self,id) -> None:
        self.vehicle_repo.delete(id)