from fastapi import APIRouter, Depends, status
from schema.detrack_id import DetrackId
from infrastructure.repository.courier import CourierRepository
from core.services.courier import CourierService
from infrastructure.models.job import job_type_enum
from datetime import date
from typing import List,Optional
from core.entity.job import Job as JobDTO
from schema.message import Message
import uuid

router = APIRouter(prefix="/courier",tags=["Courier"])

@router.get("/generate",status_code=status.HTTP_200_OK,response_model=DetrackId)
def generate_id(repo=Depends(CourierRepository)):
    return CourierService(repo).createDetrackId()

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[JobDTO])
async def get_all(detrack_id: str,type:job_type_enum,date: Optional[date] = None,repo=Depends(CourierRepository)):
    return CourierService(repo).getAllJob(detrack_id,type,date)

@router.put('/{id}/complete',status_code=status.HTTP_200_OK,response_model=Message)
async def complete(id:uuid.UUID,repo=Depends(CourierRepository)):
    CourierService(repo).jobCompleted(id)
    return {"detail":"Job update successful."}

