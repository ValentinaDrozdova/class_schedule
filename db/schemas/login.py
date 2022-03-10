from pydantic import BaseModel


class CreateLoginDTO(BaseModel):
    login: str
    password: str


class LoginDTO(BaseModel):
    id: str
    login: str
    role: str
    password: str
    expire_time: str
    access_token: str
    created_at: str
    updated_at: str


class UpdateLoginDTO(BaseModel):
    access_token: str


class AuthData(BaseModel):
    access_token: str

    class Config:
        orm_mode = True
