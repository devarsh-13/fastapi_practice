from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as _orm

connection_url = "sqlite:///./database.db"

engine = create_engine(connection_url,connect_args={"check_same_thread": False})



SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



