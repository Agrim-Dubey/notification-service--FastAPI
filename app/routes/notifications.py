from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import crud


router= APIRouter()

@router.get("/notifications")
async def get_notifications(user_id:str,db:Session = Depends(get_db)):
    notifications = crud.get_notifications_by_user(db,user_id)
    return notifications
            
            
@router.get("/notifications/unread/count")            
async def get_unread_count(user_id:str,db:Session = Depends(get_db)):
    unread_count = crud.get_unread_count(db,user_id)
    return unread_count

@router.put("/notifications/{id}/read")
async def mark_as_read(notification_id:int,db:Session = Depends(get_db)):
    notification = crud.mark_notification_as_read(db,notification_id)
    if notification:
        return True
    raise HTTPException(status_code=404, detail="Notification is not found")
     
@router.delete("/notifications/{id}")
async def delete_notification(notification_id:int,db:Session= Depends(get_db)):
    notification = crud.delete_notification(db,notification_id)
    if notification:
        return True
    raise HTTPException(status_code=404,detail="Notification not found for deletion")