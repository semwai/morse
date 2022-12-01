from pydantic import BaseModel


class TextResponse(BaseModel):
    data: str


class AlphabetResponse(BaseModel):
    data: dict
