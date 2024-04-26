from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use this URI For MySql connction by doing changes accordingly
# SQLALCHEMY_DATABASE_URL="mysql+mysqlconnector://root:password123@localhost:3306/todo_db"

#Sqlite URL
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todo.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()