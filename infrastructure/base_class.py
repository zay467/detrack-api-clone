from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column
import uuid

@as_declarative()
class Base:
    id= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()