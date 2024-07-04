from pydantic import BaseModel

class Notification(BaseModel):
    timestamp: str
    message: str
