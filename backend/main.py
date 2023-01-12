from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import service as _service, schema as _schemas



myApp = _fastapi.FastAPI()

_service.create_database()



@myApp.post("/users/", response_model=_schemas.User)
def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_service.get_db)
):
    db_user = _service.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="email is in use"
        )
    return _service.create_user(db=db, user=user)


@myApp.get("/users/", response_model=List[_schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: _orm.Session = _fastapi.Depends(_service.get_db),
):
    users = _service.get_users(db=db, skip=skip, limit=limit)
    return users


@myApp.get("/users/{user_id}", response_model=_schemas.User)
def read_user_by_id(user_id: int, db: _orm.Session = _fastapi.Depends(_service.get_db)):
    db_user = _service.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user


@myApp.post("/users/{user_id}/blogs/",response_model=_schemas.Blog)

def create_blogs(user_id:int,blog:_schemas.BlogCreate,db:_orm.Session= _fastapi.Depends(_service.get_db)):

    db_user = _service.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return _service.create_blogs(db=db,blog=blog,user_id=user_id)

@myApp.get("/blogs/", response_model=List[_schemas.Blog])
def read_blogs(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_service.get_db),
):
    blogs = _service.get_blogs(db=db, skip=skip, limit=limit)
    return blogs


@myApp.get("/blogs/{b_id}", response_model=_schemas.Blog)
def read_blog_by_id(b_id: int, db: _orm.Session = _fastapi.Depends(_service.get_db)):
    db_blogs = _service.get_blogs_by_id(db=db, blog_id=b_id)
    if db_blogs is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this blog does not exist"
        )
    return db_blogs


@myApp.delete("/blogs/{b_id}")
def delete_blog(b_id: int, db: _orm.Session = _fastapi.Depends(_service.get_db)):
    _service.delete_blog(db=db, blog_id=b_id)
    return {"message": f"successfully deleted blog with id: {b_id}"}


@myApp.put("/posts/{post_id}", response_model=_schemas.Blog)
def update_post(
    b_id: int,
    blog: _schemas.BlogCreate,
    db: _orm.Session = _fastapi.Depends(_service.get_db),
):
    return _service.update_blog(db=db, blog=blog, blog_id=b_id)


    