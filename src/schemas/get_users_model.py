from typing import List

from pydantic import BaseModel, HttpUrl


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


class SupportData(BaseModel):
    url: HttpUrl
    text: str


class GetUsersResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]
    support: SupportData


class GetSingleUserModel(BaseModel):
    data: UserData
    support: SupportData
