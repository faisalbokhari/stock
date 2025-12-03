
from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserOut
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/whoami")
def read_users_me(current_user: User = Depends(get_current_user)):
    return {"message": f"You are {current_user.username}"}

@router.get("/list", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
