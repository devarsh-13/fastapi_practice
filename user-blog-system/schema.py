from typing import List,Optional
import datetime as dt
import pydantic as pydantic

#schema structure which will use pydantic model for validation
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
    email: str = None


class UserCreate(_UserBase):
    password: str

    class Config:
        allow_none = True



class User(_UserBase):
    id: int
    
    blogs: List[Blog] = []

    class Config:
        orm_mode = True
        allow_none = True