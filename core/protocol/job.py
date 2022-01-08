from typing import Protocol

class JobProtocol(Protocol):
    def persist(self,job):
        ...

    def update(self,job):
        ...

    def list(self):
        ...

    def delete(self,job):
        ...

    def getById(self,id):
        ...