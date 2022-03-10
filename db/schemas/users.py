from uuid import UUID

from pydantic import BaseModel
from typing import Optional, Union

from db.enums.roles import Roles


class CreateUserDTO(BaseModel):
    login: str
    password: str
    role: Roles
    name: str


class UserDTO(BaseModel):
    id: Optional[Union[str, UUID]]
    login: str
    password: str
    role: Roles
    name: str
    access_token: Optional[str]

    class Config:
        orm_mode = True
