from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="KPA API Assignment")

app.include_router(router)
