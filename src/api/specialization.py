from fastapi import APIRouter, Depends
from pydantic import conint
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_db
from db.tables import Specialization
from model.element import ListResponseModel


router = APIRouter(prefix='/specializations', tags=['specializations'])


@router.get(
    '/',
    response_model=ListResponseModel,
    description='Список всех специализаций',
)
async def get_specializations(
    page: conint(gt=0) = 1,
    size: conint(gt=0, lt=11) = 10,
    db_session: AsyncSession = Depends(get_db)
):
    return await Specialization.get_all(db_session, page, size)
