from bisheng.restructure.routers import router as router_restructure
from fastapi import FastAPI


def register_restructure(app: FastAPI):
    app.include_router(router_restructure)
