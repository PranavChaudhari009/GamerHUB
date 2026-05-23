from fastapi import APIRouter,Depends,HTTPException,status
import models
import schemas
import database
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import oauth2

router = APIRouter(
    tags=['Games'],
)

@router.post("/add_games")
def add_games(request:schemas.game,db:Session=Depends(database.get_db),current_user: schemas.TokenData = Depends(oauth2.get_currentadmin)):
    new_game=models.Games(
        
        title=request.title,
        genre=request.genre,
        description=request.description

    )
    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return new_game


@router.get("/games")
def all_games(db:Session=Depends(database.get_db)):
    games = db.query(models.Games).all()

    return games

@router.get("/games/{id}")
def get_game(id,db:Session=Depends(database.get_db)):
    getgame = db.query(models.Games).filter(models.Games.id==id).first()

    if not getgame:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"game with id={id} not found"
        )
    
    return getgame


@router.delete("/games/{id}")
def delete_games(id:int,db:Session=Depends(database.get_db),current_user: schemas.TokenData = Depends(oauth2.get_currentadmin)):
    deletegames = db.query(models.Games).filter(models.Games.id==id)

    if not deletegames.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"game with id={id} not found"
        )
      
    deletegames.delete(synchronize_session=False)

    db.commit()
    return "deleted"


@router.put("/games/{id}")
def put_games(id,request:schemas.game,db:Session=Depends(database.get_db),current_user: schemas.TokenData = Depends(oauth2.get_currentadmin)):
    updategames = db.query(models.Games).filter(models.Games.id==id)

    if not updategames.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"game with id={id} not found"
        )
    
    updategames.update(request.model_dump())
    db.commit()
    return "updated"

@router.patch("/games/{id}")
def patch_games(
    id: int,
    request: schemas.gameupdate,
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(oauth2.get_currentadmin)
):
    patchgames = db.query(models.Games).filter(models.Games.id == id)

    if not patchgames.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"game with id={id} not found"
        )

    patchgames.update(request.model_dump(exclude_unset=True))
    db.commit()

    return {"message": "updated specific"}