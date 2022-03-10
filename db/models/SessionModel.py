from sqlalchemy import Column, DateTime, Text, func, Enum, CHAR
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

from db import BaseModel
from db.enums.roles import Roles


class SessionModel(BaseModel):
    __tablename__ = 'session'
    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    login = Column("login", Text, nullable=False)
    role = Column("role", Enum(Roles), nullable=False)
    name = Column("name", Text, nullable=False)
    password = Column("password", Text, nullable=False)
    expire_time = Column("expire_time", DateTime)
    access_token = Column("access_token", Text)
    created_at = Column("created_at", DateTime, default=datetime.utcnow)
    updated_at = Column("updated_at", DateTime, default=datetime.utcnow, onupdate=func.current_timestamp())

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            "id": str(self.id),
            "login": str(self.login),
            "role": str(self.role),
            "name": str(self.name),
            "password": str(self.password),
            "expire_time": str(self.expire_time),
            "access_token": self.access_token,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }
