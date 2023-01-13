from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as _orm

#connection url with db name
connection_url = "mysql+mysqlconnector://root@localhost:3306/practice"

engine = create_engine(connection_url)
 


SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# made session local and db


