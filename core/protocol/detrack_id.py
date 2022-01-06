from typing import Protocol

class DetrackIdProtocol(Protocol):
    def persist(self,user):
        ...
        