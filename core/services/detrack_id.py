from core.protocol.detrack_id import DetrackIdProtocol
import uuid

class DetrackIdService:
    def __init__(self,detrack_id_repo:DetrackIdProtocol)->None:
        self.detrack_id_repo = detrack_id_repo

    def createDetrackId(self):
        new_detrack_id = str(uuid.uuid4()).replace("-","")
        return self.detrack_id_repo.persist(new_detrack_id)
        

   