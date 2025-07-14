from pydantic import BaseModel

class LoginRequest(BaseModel):
    phone: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class FormDataResponse(BaseModel):
    name: str
    email: str
    education: str
