from typing import List
from fastapi import APIRouter, Depends, status
from schema.job_item import JobItem
from core.services.job_item import JobItemService
from core.entity.job_item import JobItem as JobItemDTO
from schema.message import Message
import uuid

router = APIRouter(prefix="/job_item",tags=["JobItem"])

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[JobItemDTO])
async def get_all(service:JobItemService=Depends(JobItemService)):
    return service.getAllJobItem()

@router.post('/',status_code=status.HTTP_200_OK,response_model=Message)
async def create(request:JobItem,service:JobItemService=Depends(JobItemService)):
    service.addJobItem(request)
    return {"detail":"Job Item create successful."}

@router.put('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
async def update(id:uuid.UUID,request:JobItem,service:JobItemService=Depends(JobItemService)):
    service.updateJobItem(id,request)
    return {"detail":"Job Item update successful."}

@router.delete('/{id}',status_code=status.HTTP_200_OK,response_model=Message)
async def delete(id:uuid.UUID,service:JobItemService=Depends(JobItemService)):
    service.deleteJobItem(id)
    return {"detail":"Job Item delete successful."}