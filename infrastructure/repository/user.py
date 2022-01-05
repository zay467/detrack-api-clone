from infrastructure.models.user import User
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from infrastructure.session import get_db
from core.entity.user import User as UserDTO

class UserRepository:
    def __init__(self,db:Session=Depends(get_db)):
        self._db = db

    def persist(self,user):
        new_user = User(**user.dict())
        self._db.add(new_user)
        self._db.flush()
        self._db.refresh(new_user)
        return new_user
        
    def readByUsername(self,username: str) -> UserDTO:
        user = self._db.query(User).filter(User.username == username).first()
        return user
