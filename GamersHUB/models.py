from database import Base
from sqlalchemy import Column,String,Integer


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer,primary_key=True,index=True)
    
    name = Column(String)
    email = Column(String)
    password=Column(String)
    role=Column(String,default="user")


class Games(Base):
    __tablename__ = "Games"    

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    genre=Column(String)
    
    description = Column(String)

class Reviews(Base):
    __tablename__ = "Reviews"

    id = Column(Integer,primary_key=True,index=True)
    title= Column(String)
    content = Column(String)
    rating = Column(String)
    game_id=Column(Integer)
    user_id = Column(Integer)


class Comment(Base):
    __tablename__ = "comments"

    id=Column(Integer,primary_key=True,index=True)
    content=Column(String)
    review_id=Column(String)
    user_id=Column(String)

class Like(Base):
    __tablename__ = "Likes"

    id = Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer)
    review_id=Column(Integer)

class Favorites(Base):
    __tablename__ = "Favorites" 

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer)
    game_id=Column(Integer)

