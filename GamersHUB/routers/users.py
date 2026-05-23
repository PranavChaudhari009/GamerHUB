from fastapi import APIRouter,Depends,HTTPException,status
import schemas
import models
import database
from sqlalchemy.orm import Session
from .hasshing import hash




router = APIRouter(
    tags=['Sign up']
)

@router.post("/users")
def create_user(request:schemas.user,
                db:Session=Depends(database.get_db)
                ):
    new_user=models.Users(
        name=request.name,
        email=request.email,
        password=hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users/{id}",response_model=schemas.showuser)
def get_user(id,db:Session=Depends(database.get_db)):
    getuser = db.query(models.Users).filter(models.Users.id==id).first()

    if not getuser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id={id} not found"
        )
    
    return getuser

