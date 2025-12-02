
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.security import create_access_token, verify_password
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/user", tags=["auth"])

FAKE_USER = {
    "username": "Admin",
    "hashed_password": "$2b$12$Tw0/m2.oEjnYewn0MZXEd.qIC1WIO.CM6wvuTNaUG64m1cGX2g2Gy"
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != FAKE_USER["username"] or not verify_password(form_data.password, FAKE_USER["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

