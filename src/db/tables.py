from fastapi import HTTPException
from sqlalchemy import (BigInteger, Column, Float, ForeignKey, Integer,
                        PrimaryKeyConstraint, String, func, select)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import attributes
from sqlalchemy.orm.exc import NoResultFound

from model.element import (ActionToolResponseModel, ElementBase,
                           ListResponseModel)

Base = declarative_base()


class ReBase(Base):
    __abstract__ = True

    def get_dict(self):
        dict_t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return dict_t

    @classmethod
    async def get_all(cls, db_session: AsyncSession, page: int, size: int):
        """
        :param db_session:
        :param page:
        :param size:
        :return:
        """
        offset = (page - 1) * size

        total_count = await db_session.execute(select(func.count(cls.id)))
        total = total_count.scalar()

        stmt = select(cls).order_by(cls.id).offset(offset).limit(size)
        result = await db_session.execute(stmt)
        instances = result.scalars().all()
        data = [ElementBase(**instance.get_dict()) for instance in instances]
        return ListResponseModel.convert(
            data=data,
            size=size,
            page=page,
            total=total
        )


class Action(ReBase):
    __tablename__ = 'actions'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)


class Specialization(ReBase):
    __tablename__ = 'specializations'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Tool(ReBase):
    __tablename__ = 'tools'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)


class ActionTools(ReBase):
    __tablename__ = 'actions_tools'

    id = Column(BigInteger, nullable=False, name="source_id")
    tax_id_actions = Column(BigInteger, ForeignKey('actions.id'), nullable=False)
    tax_id_tools = Column(BigInteger, ForeignKey('tools.id'), nullable=False)
    num_links = Column(BigInteger, name="Кол-во связей")
    num_actions = Column(BigInteger, name="Кол-во действий")
    num_tools = Column(BigInteger, name="Кол-во инструментов")
    prev_tool = Column(Float, name="Распространенность инструмента")
    prev_action = Column(Float, name="Распространенность действия")
    uniq_tool_action = Column(Float, name="Уникальность инструмента для дейс")
    uniq_action_tool = Column(Float, name="Уникальность действия для инструм")
    specificity = Column(Float, name="Специфичность")

    __table_args__ = (
        PrimaryKeyConstraint('source_id', 'tax_id_actions', 'tax_id_tools'),
    )

    column_descriptions = {
        'id': 'source_id',
        'num_links': 'Кол-во связей',
        'num_actions': 'Кол-во действий',
        'num_tools': 'Кол-во инструментов',
        'prev_tool': 'Распространенность инструмента',
        'prev_action': 'Распространенность действия',
        'uniq_tool_action': 'Уникальность инструмента для дейс',
        'uniq_action_tool': 'Уникальность действия для инструм',
        'specificity': 'Специфичность'
    }

    @classmethod
    async def get_action_tool(cls, db_session: AsyncSession, action: str, tool: str):
        """
        :param db_session:
        :param action:
        :param tool:
        :return:
        """
        try:
            stmt = await db_session.execute(select(Action.id).where(Action.name == action))
            action_id = stmt.scalars().one()
        except NoResultFound:
            raise HTTPException(status_code=400, detail="Action Not Found")
        try:
            stmt = await db_session.execute(select(Tool.id).where(Tool.name == tool))
            tool_id = stmt.scalars().one()
        except NoResultFound:
            raise HTTPException(status_code=400, detail="Tool Not Found")

        stmt = select(cls).where(cls.tax_id_actions == action_id).where(cls.tax_id_tools == tool_id)
        result = await db_session.execute(stmt)
        instance = result.scalars().first()
        if instance:
            instance_dict = attributes.instance_dict(instance)
            data = {cls.column_descriptions.get(key, key): value for key, value in instance_dict.items()}
        else:
            raise HTTPException(status_code=400, detail="no link between action and tool")

        return ActionToolResponseModel(data=data)
