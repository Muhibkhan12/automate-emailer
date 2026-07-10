from sqlalchemy import Table,Column,Integer,String,Boolean,DateTime,Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime,UTC
from cors.db import meta,engine

class Settings(Base):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(primary_key = True, index=True)
    sender_account_id : Mapped[int] = mapped_column(foreign_key = True, nullable=False)
    company_name: Mapped[str] = mapped_column(String(200))
    timezone: Mapped[datetime] = mapped_column(Datetime(timezone=True), nullable=False, default=lambda: datetime.now(UTC))
    timezone: Mapped[datetime] = mapped_column(Datetime(timezone=True), nullable=False, default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False, default=lambda: datetime.now(UTC),onupdate=lambda: datetime.now(UTC))

