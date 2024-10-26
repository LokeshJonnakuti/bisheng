from bisheng.restructure.assistants.views import router
from fastapi import APIRouter

assistant_router = APIRouter(prefix='/api/v1')
assistant_router.include_router(router)
