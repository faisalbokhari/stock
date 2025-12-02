
from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}, this is a protected route!"}
