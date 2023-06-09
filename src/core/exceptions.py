from pydantic import BaseModel


class ErrorResponseModel(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "detail": "string"
            },
        }
