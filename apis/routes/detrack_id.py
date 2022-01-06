from fastapi import APIRouter, Depends, status
from schema.detrack_id import DetrackId
from infrastructure.repository.detrack_id import DetrackIdRepository
from core.services.detrack_id import DetrackIdService

router = APIRouter(prefix="/detrackId",tags=["Detrack ID"])

@router.get("/generate",status_code=status.HTTP_200_OK,response_model=DetrackId)
def create(repo=Depends(DetrackIdRepository)):
    return DetrackIdService(repo).createDetrackId()

