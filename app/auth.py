from fastapi import HTTPException
from app.schemas import LoginRequest
from app.utils import create_access_token

# Dummy user
dummy_user = {
    "phone": "7760873976",
    "password": "to_share@123",
    "name": "Parthasarathy"
}

def authenticate_user(login_data: LoginRequest):
    if login_data.phone == dummy_user["phone"] and login_data.password == dummy_user["password"]:
        token = create_access_token({"sub": dummy_user["phone"]})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid phone or password")
