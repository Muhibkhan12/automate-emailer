from sqlalchemy import create_engine
from sqlalchemy.orm import DeclaretiveBase, sessionmaker
from cors.config import settings

DATABASE_URL = (f"mysql+pymysql://{settings.DB_USER}:"
                f"{settings.DB_PASSWORD}@"
                f"{settings.DB_HOST}:"
                f"{settings.DB_PORT}/"
                f"{settings.DB_NAME}"
                )

engine = create_engine(
    DATABASE_URL,
    echo = True
)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush=  False,
    autocommit = False,
)

class Base(DeclaretiveBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()