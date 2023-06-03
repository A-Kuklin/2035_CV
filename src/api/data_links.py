from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import ErrorResponseModel
from db.db import get_db
from db.tables import ActionTools
from model.element import ActionToolResponseModel


router = APIRouter(prefix='/action_tool', tags=['action_tool'])


@router.get(
    '/',
    response_model=ActionToolResponseModel,
    description='Данные по действию и инструменту',
    responses={
        404: {'model': ErrorResponseModel},
    }

)
async def get_actions(
    action: str,
    tool: str,
    db_session: AsyncSession = Depends(get_db)
):
    return await ActionTools.get_action_tool(db_session, action, tool)
