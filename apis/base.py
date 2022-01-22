from fastapi import APIRouter
from .routes import user
from .routes import courier
from .routes import vehicle
from .routes import job

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(courier.router)
router.include_router(vehicle.router)
router.include_router(job.router)
