from pydantic import BaseModel


class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: str
