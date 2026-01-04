from fastapi import FastAPI


app = FastAPI(title = "notification_service")
 
@app.get("/")
async def root():
    return {"message":"Notification service for agile "}

