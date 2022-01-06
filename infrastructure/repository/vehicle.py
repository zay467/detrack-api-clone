from typing import List
import json
from infrastructure.base_repo import BaseRepo
from infrastructure.models.vehicle import Vehicle
from core.entity.vehicle import Vehicle as VehicleDTO

class VehicleRepositiory(BaseRepo):
    def persist(self,vehicle) -> VehicleDTO:
        new_vehicle = Vehicle(**vehicle.dict())
        new_vehicle = self.create(new_vehicle)
        return VehicleDTO.from_orm(new_vehicle)
    
    def update(self,id,vehicle) -> VehicleDTO:
        vehicle_orm = self.read(Vehicle,id)
        updated_vehicle = super().update(vehicle_orm,vehicle.dict())
        return VehicleDTO.from_orm(updated_vehicle)
        
    def list(self) -> List[VehicleDTO]:
        vehicles = self.readAll(Vehicle)
        # vehicle_dto_list = []
        # for vehicle in vehicles:
        #     vehicle.groups = json.loads(vehicle.groups)
        #     vehicle_dto_list.append(VehicleDTO.from_orm(vehicle))
        return [VehicleDTO.from_orm(vehicle) for vehicle in vehicles]
    
    def delete(self,vehicle) -> None:
        vehicle_orm = self.read(Vehicle,vehicle.id)
        super().delete(vehicle_orm)
        
    def getById(self,id) -> VehicleDTO:
        vehicle_orm = self.read(Vehicle,id)
        return VehicleDTO.from_orm(vehicle_orm)
    