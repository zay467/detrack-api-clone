from typing import Protocol

class CourierProtocol(Protocol):
    def persist(self,detrack_id):
        ...
    
    def readByDetrackId(self,detrack_id):
        ...

    def listByAssignToIdAndTypeAndDate(self,id,type,date):
        ...

    def getVehicleIdByDetrackId(self,detrack_id):
        ...

    def listByAssignToIdAndType(self,id,type):
        ...

    def updateStatus(self,id):
        ...