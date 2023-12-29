from pydantic import BaseModel
from datetime import datetime

class Client(BaseModel):
    email: str 
    name: str 
    is_special: bool = True
    created_at: datetime 

    class Config: 
        orm_mode = True