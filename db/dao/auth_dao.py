from .base_dao import BaseDao
from ..models.SessionModel import SessionModel
from ..schemas.login import CreateLoginDTO, UpdateLoginDTO


class AuthDAO(BaseDao[SessionModel, CreateLoginDTO, UpdateLoginDTO, None]):
    pass


auth_dao = AuthDAO(SessionModel)
