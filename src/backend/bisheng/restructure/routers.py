from bisheng.restructure.assistants.routers import assistant_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(assistant_router)
