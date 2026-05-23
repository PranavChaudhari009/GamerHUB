from fastapi import APIRouter,Depends,status,HTTPException
import models,schemas,database
from sqlalchemy.orm import Session
import oauth2



router = APIRouter(
    tags=["Likes"]
)

@router.post("/reviews/{review_id}/like")
def like_review(
    review_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(oauth2.get_currentuser)
):
    existing_like = db.query(models.Like).filter(
        models.Like.review_id == review_id,
        models.Like.user_id == current_user.id
    ).first()

    if existing_like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already liked this review"
        )

    new_like = models.Like(
        review_id=review_id,
        user_id=current_user.id
    )

    db.add(new_like)
    db.commit()
    db.refresh(new_like)

    return {"message": "Review liked"}


@router.get("/reviews/{review_id}/like")
def get_like(review_id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    total_like=db.query(models.Like).filter(models.Like.review_id==review_id).count()

    return total_like


@router.delete("/reviews/{review_id}/like")
def delete_likes(review_id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    delete_like=db.query(models.Like).filter(models.Like.review_id==review_id,models.Like.user_id == current_user.id).first()

    if not delete_like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"like  ={review_id} not  found"
        )
    
    db.delete(delete_like)
    db.commit()

    return "Like deleted"