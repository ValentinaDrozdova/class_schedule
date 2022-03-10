from typing import Generic, TypeVar
from db.dao.base_dao import BaseDao, UpdateSchemaType, CreateSchemaType, DeleteSchemaType

DaoType = TypeVar("DaoType", bound=BaseDao)


class BaseAppService(Generic[DaoType, UpdateSchemaType, CreateSchemaType, DeleteSchemaType]):
    def __init__(self, dao: DaoType):
        self._dao = dao
