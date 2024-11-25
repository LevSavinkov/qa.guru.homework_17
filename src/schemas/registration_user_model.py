from pydantic import BaseModel


class RegistrationUserResponse(BaseModel):
    id: int
    token: str

class AuthorizationUserResponse(BaseModel):
    token: str
    