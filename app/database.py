from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DB_USER, DB_NAME, DB_PASSWORD, DB_HOST, DB_PORT, DATABASE_URL
SQLALCHEMY_DATABASE_URL = (
    f"{DATABASE_URL}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
