from http import HTTPStatus

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from db.schemas.login import AuthData, CreateLoginDTO
from services.login_service import login_service
from .api_spec import ApiSpec

router = InferringRouter(tags=["login"])


@cbv(router)
class LoginView:
    @router.post(ApiSpec.LOGIN,
                 response_model=AuthData)
    async def login(self, request: CreateLoginDTO):
        resp = await login_service.login(request)
        return resp
