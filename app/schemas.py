from pydantic import BaseModel
from typing import Optional,Dict,Any

class NotificationEvent(BaseModel):

    user_id : str
    type :str
    from_user_id : str
    from_user_name : str
    message : str
    data : Optional[Dict[str,Any]] = None
    created_at : str
    
    
class NotificationCreate(BaseModel):
    user_id : str
    type :str
    from_user_id : str
    from_user_name : str
    message : str
    data : Optional[Dict[str,Any]] = None
    class Config:
        orm_mode = True
        
class NotificationResponse(BaseModel):
    id:int
    user_id : str
    type :str
    from_user_id : str
    from_user_name : str
    message: str
    data : Optional[Dict[str,Any]] = None
    read : bool
    created_at : str
    updated_at : str
    class Config:
        orm_mode = True
            

