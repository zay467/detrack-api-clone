from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .jwt_token import JWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

def extract_token_data(token: str = Depends(oauth2_scheme)):
    return JWT.verify_token(token)