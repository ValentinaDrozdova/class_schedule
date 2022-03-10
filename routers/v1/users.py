from http import HTTPStatus

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from db.schemas.users import CreateUserDTO
from services.users_service import users_service
from .api_spec import ApiSpec

router = InferringRouter(tags=["users"])


@cbv(router)
class UsersView:
    @router.post(ApiSpec.USERS,
                 status_code=HTTPStatus.CREATED)
    async def create_user(self, request: CreateUserDTO):
        await users_service.create_user(request)

