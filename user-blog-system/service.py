import sqlalchemy.orm as _orm
from sqlalchemy import text
from passlib.context import CryptContext

import model as _model, schema as _schema, db as _database




def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
#function which will create db session for each request

    db  = _database.SessionLocal()

    try: 
        yield db

    finally:

        db.close()



def get_user_by_email(db:_orm.Session,email:str):

    return db.query(_model.User).filter(_model.User.email == email).first()

   
#gets the user with entered email

def create_user(db: _orm.Session, user: _schema.UserCreate):

    
   



    db_user = _model.User(email=user.email, password=user.password )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#creating user into db

def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.execute(text("SELECT * FROM user LIMIT :limit OFFSET :offset "),{'limit':limit,'offset':skip}).fetchall()

#getting all the user with  skip and limit parameters
def get_user_by_id(db: _orm.Session, user_id: int):
    return db.execute(text("SELECT * FROM user WHERE id = :id"),{'id':user_id}).fetchone()

#getting a user with entered id
def create_blogs(db:_orm.Session,blog:_schema.BlogCreate,user_id:int):

    db_blog=_model.Blogs(**blog.dict(),u_id = user_id)

    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)


    return db_blog

#same process for blog
def get_blogs(db:_orm.Session,skip:int = 0,limit:int = 10):

    return db.query(_model.Blogs).offset(skip).limit(limit).all()

def get_blogs_by_id(db: _orm.Session, blog_id: int):

    return db.query(_model.Blogs).filter(_model.Blogs.b_id == blog_id).first()

#delete blog by id
def delete_blog(db: _orm.Session, blog_id: int):
    db.query(_model.Blogs).filter(_model.Blogs.b_id == blog_id).delete()
    db.commit()

#updating blog using put request
def update_blog(db: _orm.Session, blog_id: int, blog: _schema.BlogCreate):
    db_blog = get_blogs_by_id(db=db, blog_id=blog_id)
    db_blog.b_title = blog.b_title
    db_blog.b_desc = blog.b_desc
    db.commit()
    db.refresh(db_blog)
    return db_blog









