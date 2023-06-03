from fastapi import APIRouter, Depends
from pydantic import conint
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_db
from db.tables import Tool
from model.element import ListResponseModel


router = APIRouter(prefix='/tools', tags=['tools'])


@router.get(
    '/',
    response_model=ListResponseModel,
    description='Список всех инструментов',
)
async def get_tools(
    page: conint(gt=0) = 1,
    size: conint(gt=0, lt=11) = 10,
    db_session: AsyncSession = Depends(get_db)
):
    return await Tool.get_all(db_session, page, size)
