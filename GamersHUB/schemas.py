from pydantic import BaseModel
from typing import Optional


class user(BaseModel):
    
    name:str
    email:str
    password:str

class game(BaseModel):
    
    title:str
    genre:str 
    description:str  

class gameupdate(BaseModel):
    title:Optional[str]=None
    genre:Optional[str]=None
    description:Optional[str]=None


class user(BaseModel):
    name:str
    email:str
    password:str    

class showuser(BaseModel):
    name:str
    email:str    
    role:str

    class Config:
       orm_mode = True
                   

class login(BaseModel):
    email:str
    password:str      


class TokenData(BaseModel):
    id:int | None = None
    email: str | None = None    
    role: str | None = None   



class reviews(BaseModel):
    title:str
    content:str
    rating:str


class comment(BaseModel):
    content:str

class showfavorite(BaseModel):
    game_id:int 

    class config:
        orm_model=True       
    
