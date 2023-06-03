from pydantic import BaseModel


class PaginatedMetaDataModel(BaseModel):
    total: int
    page: int
    size: int


class ElementBase(BaseModel):
    id: int
    name: str


class ListMetaDataModel(BaseModel):
    pagination: PaginatedMetaDataModel


class ListResponseModel(BaseModel):
    data: list[ElementBase]
    meta: ListMetaDataModel

    @staticmethod
    def convert(data, size, page, total):
        return ListResponseModel(
            data=data,
            meta=ListMetaDataModel(
                pagination=PaginatedMetaDataModel(
                    total=total,
                    page=page,
                    size=size
                )
            )
        )


class ActionToolResponseModel(BaseModel):
    data: dict





