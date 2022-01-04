from typing import List
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from infrastructure.base import Base, User
from .session import get_db
# from dependencies.user import get_current_user
from exceptions.http import NOT_FOUND
from exceptions.repo import SQLALCHEMY_ERROR

class BaseRepo:
    def __init__(self,db:Session=Depends(get_db),user:User=Depends(get_current_user)):
        self._db = db
        self._user = user

    def readAll(self,model:Base) -> List[Base]:
        try:
            return self._db.query(model).all()
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def read(self,model:Base,id:int) -> Base:
        try:
            data = self._db.query(model).get(id)
            if data is None:
                raise NOT_FOUND
            return data
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def create(self,model:Base) -> Base:
        try:
            model.create_stamp(self._user)
            self._db.add(model)
            self._db.flush()
            self._db.refresh(model)
            return model
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def update(self,model:Base,data:dict) -> Base:
        try:
            for key,value in data.items():
                    setattr(model,key,value)
            model.update_stamp(self._user)
            return model
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def delete(self,model:Base) -> None:
        try:
            self._db.delete(model)
            self._db.flush()
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)
 