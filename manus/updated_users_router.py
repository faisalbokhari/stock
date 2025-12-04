from fastapi import APIRouter, Depends
from app.dependencies import get_current_user, get_db, require_admin_role # Import NEW dependency
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserOut
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/whoami")
def read_users_me(current_user: User = Depends(get_current_user)):
    return {"message": f"You are {current_user.username}"}

# VULNERABILITY REMEDIATION: Added Depends(require_admin_role)
@router.get("/list", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db), current_user: User = Depends(require_admin_role)):
    return db.query(User).all()
