from sqlalchemy import Table,Column,Integer,String,Float,Boolean,Unique,DateTime,Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime,UTC
from cors.db import meta,engine

class User(Base):
    __tablename__ = "users",

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255),unique=True,index=True)
    password: Mapped[str] = mapped_column(String(255))
    email_verification : Mapped[bool] = mapped_column(Boolean, nullable=False, default = False, server_default = 0)
    verification_token : Mapped[str] = mapped_column(String(255),nullable=True)
    jwt_token : Mapped[str | None] = mapped_column(Text,nullable = True)
    created_at : Mapped[datetime] = mapped_column(DateTime,nullable=False,default=datetime.UTC.now)
    updated_at : Mapped[datetime] = mapped_column(DateTime,nullable=False,default=datetime.utcnow,onupdate=datetime.utcnow)


meta.create_all(engine)
conn = engine.connect()
