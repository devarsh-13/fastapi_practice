import sqlalchemy.orm as _orm

import model as _model, schema as _schema, db as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():


    db  = _database.SessionLocal()

    try: 
        yield db

    finally:

        db.close()



def get_user_by_email(db:_orm.Session,email:str):

    return db.query(_model.User).filter(_model.User.email == email).first()


def create_user(db: _orm.Session, user: _schema.UserCreate):
    fake_hashed_password = user.password + "thisisnotsecure"
    db_user = _model.User(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_model.User).offset(skip).limit(limit).all()


def get_user_by_id(db: _orm.Session, user_id: int):
    return db.query(_model.User).filter(_model.User.id == user_id).first()


def create_blogs(db:_orm.Session,blog:_schema.BlogCreate,user_id:int):

    db_blog=_model.Blogs(**blog.dict(),u_id = user_id)

    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)


    return db_blog


def get_blogs(db:_orm.Session,skip:int = 0,limit:int = 10):

    return db.query(_model.Blogs).offset(skip).limit(limit).all()

def get_blogs_by_id(db: _orm.Session, blog_id: int):

    return db.query(_model.Blogs).filter(_model.Blogs.b_id == blog_id).first()

def delete_blog(db: _orm.Session, blog_id: int):
    db.query(_model.Blogs).filter(_model.Blogs.b_id == blog_id).delete()
    db.commit()


def update_blog(db: _orm.Session, blog_id: int, blog: _schema.BlogCreate):
    db_blog = get_blogs_by_id(db=db, blog_id=blog_id)
    db_blog.b_title = blog.b_title
    db_blog.b_desc = blog.b_desc
    db.commit()
    db.refresh(db_blog)
    return db_blog









