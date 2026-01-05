import json
from fastapi import WebSocket
from typing import Dict 




class WebsocketManager():
    def __init__(self):
        self.active_connections : Dict[str,WebSocket]={}
    
    async def connect(self, user_id:str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id]=websocket
        
    async def disconnect(self,user_id:str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
            
    
    async def send_notifications(self,user_id:str,message:dict):
        if user_id in self.active_connections:
            websocket = self.active_connections[user_id]
            try:
                await websocket.send_json(message)
            except Exception as e:
                await self.disconnect(user_id)
        
    def is_user_online(self, user_id:str):
        if user_id in self.active_connections:
            return True
        return False
    
manager = WebsocketManager()