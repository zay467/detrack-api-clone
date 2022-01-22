from core.protocol.courier import CourierProtocol
import uuid

class CourierService:
    def __init__(self,courier_repo:CourierProtocol)->None:
        self.courier_repo = courier_repo

    def createDetrackId(self):
        new_detrack_id = str(uuid.uuid4()).replace("-","")
        return self.courier_repo.persist(new_detrack_id)
        
    def getAllJob(self,detrack_id,type,date):
        vehicle_id = self.courier_repo.getVehicleIdByDetrackId(detrack_id)
        if date is None:
            return self.courier_repo.listByAssignToIdAndType(vehicle_id,type)
        return self.courier_repo.listByAssignToIdAndTypeAndDate(vehicle_id,type,date)
   
    def jobCompleted(self,id):
        self.courier_repo.updateStatus(id)
        return