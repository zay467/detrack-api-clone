from fastapi import APIRouter
from .routes import user
from .routes import detrack_id

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(detrack_id.router)
