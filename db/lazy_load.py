from sqlalchemy.orm import selectinload


async def lazy_load(operation,
                    model,
                    inner_object,
                    selector,
                    session
                    ):
    inner_objects = []
    if isinstance(inner_object, list):
        inner_objects.extend(inner_object)
    else:
        inner_objects.append(inner_object)

    stmt = operation(model). \
        options(selectinload(*inner_objects)). \
        where(model.id == selector)
    result = await session.execute(stmt)
    return result.scalar()
