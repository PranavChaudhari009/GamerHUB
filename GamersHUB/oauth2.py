from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends,HTTPException,status
import jwttoken



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_currentuser(data:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return jwttoken.verify_token(data, credentials_exception)


def get_currentadmin(
    current_user = Depends(get_currentuser)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access only"
        )

    return current_user