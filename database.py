from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "postgresql://fastapi_user:fastapi_user_password@127.0.0.1:5432/wardrobe_fastapi" # TODO 
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/wardrobe_fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
