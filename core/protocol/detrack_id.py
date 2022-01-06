from typing import Protocol

class DetrackIdProtocol(Protocol):
    def persist(self,detrack_id):
        ...
    
    def readByDetrackId(self,detrack_id):
        ...