from typing import List
from fastapi import APIRouter, Depends, status
from schema.job import Job
from core.services.job import JobService
from core.entity.job import Job as JobDTO
from schema.message import Message
import uuid

router = APIRouter(prefix="/job",tags=["Job"])

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[JobDTO])
async def get_all(service:JobService=Depends(JobService)):
    return service.getAllJob()

@router.post('/',status_code=status.HTTP_200_OK,response_model=Message)
async def create(request:Job,service:JobService=Depends(JobService)):
    service.addJob(request)
    return {"detail":"Job create successful."}

# @router.put('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
# async def update(id:uuid.UUID,request:Job,service:JobService=Depends(JobService)):
#     service.updateJob(id,request)
#     return {"detail":"Job update successful."}

# @router.delete('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
# async def delete(id:uuid.UUID,service:JobService=Depends(JobService)):
#     service.deleteJob(id)
#     return {"detail":"Job delete successful."}