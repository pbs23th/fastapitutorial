from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from backend.db.session import get_db
from backend.db.repository.users import create_new_user
from backend.schemas.users import UserCreate,ShowUser

router = APIRouter()


@router.post("/",response_model = ShowUser)
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user
