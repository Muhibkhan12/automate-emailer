from sqlalchemy import String,Boolean,DateTime,Text,text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime,UTC
from app.cors.db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255),unique=True,index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column( DateTime(timezone=True),  nullable=False,  default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False, default=lambda: datetime.now(UTC),onupdate=lambda: datetime.now(UTC)
)