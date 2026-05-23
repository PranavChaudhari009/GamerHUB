from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
import database
import models
import schemas
import oauth2



router = APIRouter(
    tags=["Reviews"]

)


@router.post("/reviews/{game_id}")
def add_reviews(game_id:int,request:schemas.reviews,db:Session=Depends(database.get_db),current_user = Depends(oauth2.get_currentuser),):
    reviews=models.Reviews(
        title=request.title,
        content=request.content,
        rating=request.rating,
        game_id=game_id,
        user_id=current_user.id
    )

    db.add(reviews)
    db.commit()
    db.refresh(reviews)

    return reviews

@router.get("/reviews")
def all_reviews(db:Session=Depends(database.get_db),current_user =Depends(oauth2.get_currentuser)):
    reviews=db.query(models.Reviews).all()

    return reviews


@router.get("/reviews/{id}")
def get_reviews(id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    getreviews=db.query(models.Reviews).filter(models.Reviews.id==id).first()

    if not getreviews:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"reviews with id ={id} not found"
        )
    
    return getreviews

@router.put("/reviews/{id}")
def update_reviews(id:int,request:schemas.reviews,db:Session=Depends(database.get_db),current_user =Depends(oauth2.get_currentuser)):
    updatereviews = db.query(models.Reviews).filter(models.Reviews.id==id)

    if not updatereviews.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"review with id {id} not found"
            
        )
    updatereviews.update(request.model_dump())
    db.commit()

    return "updated"


@router.delete("/reviews/{id}")
def delete_reviews(id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    delete=db.query(models.Reviews).filter(models.Reviews.id==id)

    if not delete.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"reviews with id ={id} not found"
        )
    
    delete.delete(synchronize_session=False)

    db.commit()
    return delete


@router.patch("/reviews/{id}")
def specific_update(id:int,request:schemas.reviews,db:Session=Depends(database.get_db)):
    patchupdated = db.query(models.Reviews).filter(models.Reviews.id==id)


    if not patchupdated.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"review with id ={id} not found"
        )
    patchupdated.update(request.model.Dump(exclude_unset=True))
    db.commit()
    return "updated"
