from typing import List
from fastapi import APIRouter, Depends, status
from schema.vehicle import Vehicle
from core.services.vehicle import VehicleService
from core.entity.vehicle import Vehicle as VehicleDTO
from schema.message import Message
import uuid

router = APIRouter(prefix="/vehicle",tags=["Vehicle"])

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[VehicleDTO])
async def get_all(service:VehicleService=Depends(VehicleService)):
    return service.getAllVehicle()

@router.post('/',status_code=status.HTTP_200_OK,response_model=Message)
async def create(request:Vehicle,service:VehicleService=Depends(VehicleService)):
    service.addVehicle(request)
    return {"detail":"Vehicle create successful."}

@router.put('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
async def update(id:uuid.UUID,request:Vehicle,service:VehicleService=Depends(VehicleService)):
    service.updateVehicle(id,request)
    return {"detail":"Vehicle update successful."}

@router.delete('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
async def delete(id:uuid.UUID,service:VehicleService=Depends(VehicleService)):
    service.deleteVehicle(id)
    return {"detail":"Vehicle delete successful."}