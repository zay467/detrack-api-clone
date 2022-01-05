from typing import Protocol

class UserProtocol(Protocol):
    def persist(self,user):
        ...
        
    def readByUsername(self,username):
        ...