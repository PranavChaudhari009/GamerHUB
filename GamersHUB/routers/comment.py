from fastapi import APIRouter,HTTPException,status,Depends
import database,schemas,models
from sqlalchemy.orm import Session
import oauth2


router = APIRouter(
    tags=["Comments"]
)


@router.post("/comments/{review_id}")
def comments(review_id:int,request:schemas.comment,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    new_comments=models.Comment(
        content=request.content,
        review_id=review_id,
        user_id=current_user.id
    )

    db.add(new_comments)
    db.commit()
    db.refresh(new_comments)

    return new_comments


@router.get("/comments")
def get_comments(db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    comments = db.query(models.Comment).all()

    return comments

@router.get("/comment/{id}")
def get_comments(id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    comments = db.query(models.Comment).filter(models.Comment.id==id).first()

    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comment with id ={id} not found"

        )
    
    return comments

@router.put("/commnets/{id}")
def update(id:int,request:schemas.comment,db:Session=Depends(database.get_db),current_user =Depends(oauth2.get_currentuser)):
    updatecomments=db.query(models.Comment).filter(models.Comment.id==id)
    
    if not updatecomments.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comments with id = {id} not found"
   
        )
    updatecomments.update(request.model_dump())
    db.commit()
    return "updated"


@router.delete("/comments/{id}")
def delete(id:int,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    deletecomments=db.query(models.Comment).filter(models.Comment.id==id)

    if not deletecomments.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'comment with id ={id} not found'
        )
    
    deletecomments.delete(synchronize_session=False)

    return "deleted"

    
@router.patch("/comments/{id}")
def specificupdate(id:int,request:schemas.comment,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_currentuser)):
    update_Comment=db.query(models.Comment).filter(models.Comment.id==id)

    if not update_Comment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comments with id={id} not found"
        )
    
    update_Comment.update(request.model_dump(exclude_unset=True))
    db.commit()
    
    return "updated specific values"