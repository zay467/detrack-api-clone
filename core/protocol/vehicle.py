from typing import Protocol

class VehicleProtocol(Protocol):
    def persist(self,vehicle):
        ...

    def update(self,vehicle):
        ...

    def list(self):
        ...

    def delete(self,vehicle):
        ...

    def getById(self,id):
        ...
        
    