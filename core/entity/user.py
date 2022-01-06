from pydantic import BaseModel
import uuid

class User(BaseModel):
    id: uuid.UUID
    username: str
    password: str
    role: str
    class Config():
        orm_mode = True