from datetime import datetime, timedelta
from http import HTTPStatus

import jwt
from fastapi import HTTPException

from db.dao.auth_dao import AuthDAO, auth_dao
from db.models.SessionModel import SessionModel
from db.schemas.login import CreateLoginDTO, AuthData, UpdateLoginDTO
from services.base_app_service import BaseAppService
from settings.settings import settings


class LoginService(
                   BaseAppService[AuthDAO, None, CreateLoginDTO, None]):
    async def login(self, request: CreateLoginDTO) -> SessionModel:
        result = await auth_dao.get_by(SessionModel.login, request.login)
        result = [row[0] for row in result][0]
        print(result)
        if result.password == request.password:
            access_token_payload = {
                'exp': datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_DELTA),
                'iat': datetime.utcnow(),
            }
            access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256')
            updated_model = await auth_dao.update(result.id, UpdateLoginDTO(access_token=access_token))
            return AuthData.from_orm(updated_model)

        raise HTTPException(HTTPStatus.FORBIDDEN)


login_service = LoginService(auth_dao)
