from fastapi import FastAPI
from contextlib import asynccontextmanager
import threading
from app.kafka.consumer import start_consumer

@asynccontextmanager
async def lifespan(app: FastAPI):
    t = threading.Thread(target=start_consumer, daemon=True)
    t.start()
    yield

app = FastAPI(lifespan=lifespan)
