from typing import List
import datetime as dt
import pydantic as pydantic


class _BlogBase(pydantic.BaseModel):
    b_title: str
    b_desc: str


class BlogCreate(_BlogBase):
    pass


class Blog(_BlogBase):
    b_id: int
    u_id: int
    b_created: dt.datetime
    

    class Config:
        orm_mode = True

 
class _UserBase(pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str


class User(_UserBase):
    id: int
    
    blogs: List[Blog] = []

    class Config:
        orm_mode = True