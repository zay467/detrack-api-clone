from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schema.message import Message
from schema.user import User
from schema.token import Token, RefreshToken
from infrastructure.session import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/user",tags=["User"])

@router.post("/",status_code=status.HTTP_200_OK,response_model=Message)
def create(request:User,db:Session = Depends(get_db)):
    return {"detail":"User create successful."}

@router.post("/login",response_model=Token)
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    pass

@router.post("/refreshToken",response_model=Token)
def refresh_token(request:RefreshToken):
    pass
