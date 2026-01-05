from pydantic import BaseSettings

class Settings(BaseSettings):
    
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_DB:str
    DATABASE_URL:str 
    RABBITMQ_URL: str
    
    class Config:
        env_file = ".env"
        
        
settings = Settings()

