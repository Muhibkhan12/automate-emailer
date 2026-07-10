from sqlalchemy import Table,Column,Integer,String,Boolean,DateTime,Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from cors.db import mera,engine

class Settings(Base):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(primary_key = True, index=True),
    company_name 