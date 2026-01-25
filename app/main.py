from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routes import websockets, notifications
from app.rabbitmq_consumer import start_consumer_thread
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_consumer_thread()
    
    yield  

app = FastAPI(title="notification_service", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(websockets.router)
app.include_router(notifications.router)
@app.get("/")
async def root():
    return {"message": "Notification service for agile"}