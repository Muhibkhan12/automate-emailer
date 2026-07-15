from sqlalchemy import Table,Column,Integer,String,Boolean,DateTime,Text, ForeignKey,
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.cors.db import Base
from datetime import datetime,UTC
from cors.db import meta,engine

class Settings(Base):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(primary_key = True, index=True)
    default_sender_account_id : Mapped[int] = mapped_column(ForeignKey("default_sender_account_id"))
    company_name: Mapped[str] = mapped_column(String(200))
    timezone: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(UTC))
# Add missing created_at column to match migration.
    updated_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True),nullable=False, default=lambda: datetime.now(UTC),onupdate=lambda: datetime.now(UTC))

