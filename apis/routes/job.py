from typing import List,Optional
from fastapi import APIRouter, Depends, status
from schema.job import Job
from schema.job_item import JobItem
from core.services.job import JobService
from core.entity.job import Job as JobDTO
from schema.message import Message
from infrastructure.models.job import job_type_enum
from datetime import date
import uuid

router = APIRouter(prefix="/job",tags=["Job"])

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[JobDTO])
async def get_all(type:job_type_enum,date: Optional[date] = None,service:JobService=Depends(JobService)):
    return service.getAllJob(type,date)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=JobDTO)
async def get(id:uuid.UUID,service:JobService=Depends(JobService)):
    return service.getJobByID(id)

@router.post('/',status_code=status.HTTP_200_OK,response_model=Message)
async def create(request:Job,service:JobService=Depends(JobService)):
    service.createJob(request)
    return {"detail":"Job create successful."}

@router.post('/{job_id}/item',status_code=status.HTTP_200_OK,response_model=Message)
async def create_item(job_id:uuid.UUID,request:JobItem,service:JobService=Depends(JobService)):
    service.createJobItem(job_id,request)
    return {"detail":"Job Item create successful."}

@router.put('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
async def update(id:uuid.UUID,request:Job,service:JobService=Depends(JobService)):
    service.updateJob(id,request)
    return {"detail":"Job update successful."}
    
@router.put('/item/{job_item_id}',status_code=status.HTTP_200_OK,response_model=Message)
async def update_item(job_item_id:uuid.UUID,request:JobItem,service:JobService=Depends(JobService)):
    service.updateJobItem(job_item_id,request)
    return {"detail":"Job Item update successful."}

@router.delete('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
async def delete(id:uuid.UUID,service:JobService=Depends(JobService)):
    service.deleteJob(id)
    return {"detail":"Job delete successful."}

@router.delete('/item/{job_item_id}',status_code=status.HTTP_200_OK,response_model=Message)
async def delete_item(job_item_id:uuid.UUID,service:JobService=Depends(JobService)):
    service.deleteJobItem(job_item_id)
    return {"detail":"Job Item delete successful."}