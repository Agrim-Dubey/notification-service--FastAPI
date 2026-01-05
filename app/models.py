from app.database import Base
from sqlalchemy import Column,Integer,String,DateTime,JSON,Text,Boolean
from datetime import datetime,timezone




class Notification(Base):
    __tablename__="notifications"
    
    id = Column(Integer,primary_key = True,index = True )
    user_id = Column(String, index=True , nullable = False)
    type = Column(String, nullable = False)
    from_user_id = Column(String,nullable =False)
    from_user_name = Column(String,nullable = False)
    message = Column(Text,nullable =False)
    data = Column(JSON, nullable = True)
    read = Column(Boolean, default = False, nullable = False)
    created_at = Column(DateTime, default = datetime.now(timezone.utc), nullable = False)
    updated_at = Column(DateTime, default = datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable = False)