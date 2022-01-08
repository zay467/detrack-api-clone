from typing import Protocol

class JobItemProtocol(Protocol):
    def persist(self,job_item):
        ...

    def update(self,job_item):
        ...

    def list(self):
        ...

    def delete(self,job_item):
        ...

    def getById(self,id):
        ...