from fastapi import FastAPI,Depends,HTTPException,status,Response

from database import get_db,Base,engine
from sqlalchemy.orm import Session
import models
import schemas
import database
# from .hasshing import hash
from routers import games,users,login,reviews,comment,like,favorite
app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(users.router)
app.include_router(games.router)


app.include_router(reviews.router)
app.include_router(comment.router)
app.include_router(favorite.router)
app.include_router(like.router)




