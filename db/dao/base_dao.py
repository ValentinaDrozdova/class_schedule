from loguru import logger

from db import SessionLocal, BaseModel
from pydantic import BaseModel as BaseSchema
from sqlalchemy import select, update, delete
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc
from typing import Generic, TypeVar, Type, Optional, Any, List

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseSchema)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseSchema)
DeleteSchemaType = TypeVar("DeleteSchemaType", bound=BaseSchema)


class BaseDao(Generic[ModelType, CreateSchemaType, UpdateSchemaType, DeleteSchemaType]):
    def __init__(self, model: Type[ModelType], session_generator: Type[AsyncSession] = SessionLocal):
        self._model = model
        self._session_generator = session_generator

    async def create(self, create_obj: CreateSchemaType) -> Optional[ModelType]:
        logger.info(f"{self._model.__name__} DAO: Create db entry")
        logger.trace(f"{self._model.__name__} DAO: Data passed for creation: {create_obj}")
        db_model = self._model(**create_obj.dict(exclude_unset=True))
        async with self._session_generator() as session:
            session.add(db_model)
            await session.commit()
            await session.refresh(db_model)
            return db_model

    async def update(self, obj_id: str, update_obj: UpdateSchemaType) -> Optional[ModelType]:
        logger.info(f"{self._model.__name__} DAO: Update db entry")
        logger.trace(
            f"{self._model.__name__} DAO: Data passed for creation: obj_id: {obj_id}, update_obj: {update_obj}")
        async with self._session_generator() as session:
            await session.execute(update(self._model).
                                  where(self._model.id == obj_id).
                                  values(update_obj.dict(exclude_unset=True)))
            await session.commit()
            return await session.get(self._model, obj_id)

    async def get(self, obj_id: str) -> Optional[ModelType]:
        logger.info(f"{self._model.__name__} DAO: Get db entry. Passed data: obj_id {obj_id}")
        async with self._session_generator() as session:
            return await session.get(self._model, obj_id)

    async def get_by(self, obj_attr: InstrumentedAttribute, attr: Any) -> Optional[ModelType]:
        logger.info(f"{self._model.__name__} DAO: Get db entry. Passed data: obj_attr {obj_attr}, attr {attr}")
        async with self._session_generator() as session:
            return await session.execute(select(self._model).where(obj_attr == attr))

    async def get_all(self, offset: int = 0, limit: int = 20, filters: Optional[dict] = None) -> List[ModelType]:
        logger.info(f"{self._model.__name__} DAO: Get all db entries")
        async with self._session_generator() as session:
            expr = select(self._model).offset(offset).limit(limit).order_by(desc(self._model.created_at))
            if filters:
                expr = expr.filter_by(**filters)
            db_objects = await session.execute(expr)
            return [raw[0] for raw in db_objects]

    async def delete(self, obj_id: str):
        async with self._session_generator() as session:
            await session.execute(delete(self._model).where(self._model.id == obj_id))
            await session.commit()
