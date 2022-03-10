from .base_dao import BaseDao
from ..models.SessionModel import SessionModel
from ..schemas.users import CreateUserDTO, UserDTO


class UsersDAO(BaseDao[SessionModel, CreateUserDTO, None, UserDTO]):
    pass


users_dao = UsersDAO(SessionModel)
