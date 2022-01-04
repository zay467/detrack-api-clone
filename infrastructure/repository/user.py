from infrastructure.base_repo import BaseRepo
from infrastructure.models.user import User

class UserRepository(BaseRepo):
    def persist(self,user):
        pass
        
    def readByUsername(self,username: str) :
        pass
