from fastapi import HTTPException,status

NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail= 'Resoucse not found'
)

INVALID_CREDENTIAL = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

BAD_REQUEST = lambda message: HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail=message
)