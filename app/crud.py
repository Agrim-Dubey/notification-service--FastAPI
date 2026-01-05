from sqlalchemy.orm import Session
from app.models import Notification
from app.schemas import NotificationCreate



def create_notification(db:Session,notification: NotificationCreate):
    stored_notification = Notification(**notification.model_dump())
    db.add(stored_notification)
    db.commit()
    db.refresh(stored_notification)
    return stored_notification

def get_notifications_by_user(db:Session, user_id:str, skip:int =0,limit:int = 50):
    user_notifications = db.query(Notification).filter(Notification.user_id==user_id).order_by(Notification.created_at.desc()).offset(skip).limit(limit).all()
    return user_notifications

def get_notification_by_id(db:Session,notification_id:int):
    notification= db.query(Notification).filter(Notification.id==notification_id).first()
    return notification
    
def mark_notification_as_read(db:Session,notification_id:int):
    notification = db.query(Notification).filter(Notification.id==notification_id).first()
    if notification:
        notification.read =True
        db.commit()
        return notification
    return None 

def delete_notification(db:Session,notification_id:int):
    notification=db.query(Notification).filter(Notification.id==notification_id).first()
    if notification:
        db.delete(notification)
        db.commit()
        return True
    return False

def get_unread_count(db:Session,user_id:str):
    count= db.query(Notification).filter(Notification.user_id==user_id,Notification.read==False).count()
    return count