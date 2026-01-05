from sqlalchemy.orm import Session
from app import crud, schemas
from app.websocket_manager import manager
import asyncio



def process_notification_event( event_data:dict,db:Session):
    notification = schemas.NotificationCreate(**event_data)
    saved_notification = crud.create_notification(db,notification)
    user_id= event_data['user_id']
    if manager.is_user_online(user_id):
        notification_message = {"id":saved_notification.id,
                                "type":saved_notification.type,
                                "from_user_name":saved_notification.from_user_name,
                                "message":saved_notification.message,
                                "data":saved_notification.data,
                                "created_at":saved_notification.created_at.isoformat()}                         
        
        asyncio.run(manager.send_notification(user_id, notification_message))    
    else:
        print(f"user {user_id} is offline - notification saved inside the database for  now")
    

    if event_data["type"]=="project.invited":
        print(f"will write this code in the later part")
        
