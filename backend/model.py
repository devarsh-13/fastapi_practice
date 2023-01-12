import sqlalchemy as _sql

import sqlalchemy.orm as _orm


import db as _database
 
import datetime as dt



class User(_database.Base):

    __tablename__ = "user"

    id = _sql.Column(_sql.Integer,primary_key = True, index = True,autoincrement = True)

    email = _sql.Column(_sql.String,unique = True,index = True)

    password = _sql.Column(_sql.VARCHAR(100))

    dob = _sql.Column(_sql.DateTime)

    blogs =   _orm.relationship("Blogs",back_populates = "users")



class Blogs(_database.Base):

     __tablename__ = "blogs"

     b_id  = _sql.Column(_sql.Integer,primary_key = True, index = True)

     b_title  = _sql.Column(_sql.String(20),unique = True,index = True)

     b_desc = _sql.Column(_sql.String(20))

     b_created = _sql.Column(_sql.DateTime,default = dt.datetime.now)



     u_id = _sql.Column(_sql.Integer,_sql.ForeignKey("user.id"))


     users = _orm.relationship("User", back_populates="blogs")







