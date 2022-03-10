from db.dao.users_dao import users_dao, UsersDAO
from db.models.SessionModel import SessionModel
from db.schemas.users import CreateUserDTO, UserDTO
from services.base_app_service import BaseAppService


class UsersService(
                   BaseAppService[UsersDAO, None, CreateUserDTO, None]):
    async def create_user(self, request: CreateUserDTO) -> SessionModel:
        users_schema = UserDTO(login=request.login,
                               password=request.password,
                               role=request.role,
                               name=request.name)
        return await self._dao.create(users_schema)


users_service = UsersService(users_dao)
