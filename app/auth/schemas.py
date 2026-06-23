from pydantic import BaseModel


class DealerCreate(BaseModel):
    name: str
    email: str
    password: str


class DealerResponse(BaseModel):
    id: str
    name: str
    email: str
    role: str


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
