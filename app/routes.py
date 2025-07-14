from fastapi import APIRouter, Depends, Header, HTTPException
from app.schemas import LoginRequest, TokenResponse, FormDataResponse
from app.auth import authenticate_user
from app.utils import verify_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(login_data: LoginRequest):
    return authenticate_user(login_data)

@router.get("/getformdata", response_model=FormDataResponse)
def get_form_data(authorization: str = Header(None)):
    print("Authorization Header:", authorization)
    
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = authorization.split(" ")[1]
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    return {
        "name": "Parthasarathy",
        "email": "partha@example.com",
        "education": "B.E. Electronics and Communication"
    }
