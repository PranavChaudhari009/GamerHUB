from fastapi import HTTPException,Depends,APIRouter,status
import models,schemas,database,oauth2
from sqlalchemy.orm import Session
from typing import List


router=APIRouter(tags=["Favorite"])


@router.post("/favorite/{game_id}")
def favorite(game_id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    favorite_games=db.query(models.Favorites).filter(models.Favorites.game_id==game_id,models.Favorites==current_user.id)

    if  favorite_games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"game already in favorites"
        )
    
    new_favorite=models.Favorites(
        game_id=game_id,
        user_id=current_user.id
    )

    db.add(new_favorite)
    db.commit()
    db.refresh(new_favorite)

    return "Game add to favorite"

@router.get("/my-favorite",response_model=List[schemas.showfavorite])
def get_favorite(db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):

    favorite=db.query(models.Favorites).filter(models.Favorites.user_id==current_user.id).all()

    return favorite

@router.delete("/favorite/{game_id}")
def get_favorates(game_id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    favorite=db.query(models.Favorites).filter(models.Favorites.game_id==game_id,models.Favorites.user_id==current_user.id).first()

    if not favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"favorite not found"
        

        )
        

     

    db.delete(favorite)
    db.commit()
    return "deleted"



