from fastapi import APIRouter,Depends,status,HTTPException
import schemas
import models
from .hasshing import hash
import database
from sqlalchemy.orm import Session 
import jwttoken
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email==request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"invalid credentials"
        )
    
    if not hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"invalid password"
        )
    
    access_token = jwttoken.create_access_token(
        data={"sub":user.email,
              "role":user.role,
              "id":user.id}
    )

    return {
        "access_token":access_token,
        "token_type": "bearer"
    }


import oauth2

@router.get("/profile")
def profile(current_user: schemas.TokenData = Depends(oauth2.get_currentuser)):
    return current_user