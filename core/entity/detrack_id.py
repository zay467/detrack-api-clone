from pydantic import BaseModel
import uuid

class DetrackId(BaseModel):
    id: uuid.UUID
    detrack_id:str
    class Config():
        orm_mode = True