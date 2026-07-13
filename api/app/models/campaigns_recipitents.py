from sqlalchemy import Integer,String,DateTime,Boolean,ForeignKey,Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import UTC,datetime
from cors.db import Base

class CampaignsRecipitents(Base):
    __tablename__ = "Campaigns_recipitents"
    id : Mapped[int] = mapped_column(primary_key=True)
    campaign_id : Mapped[int] = mapped_column(ForeignKey=True,nullable=False)
    sender_account_id : Mapped[int] = mapped_column(ForeignKey=True,nullable=False)
    recipitent_name : Mapped[str] = mapped_column(String(255),nullable=False)
    recipitent_email : Mapped[str] = mapped_column(String(255),unique=True)
    company : Mapped[str] = mapped_column(String(400),nullable=False)
    phone : Mapped[str] = mapped_column(String(100),nullable=False)
    status : Mapped[str] = mapped_column(String(100),nullable=False)
    retry_count : Mapped[int] = mapped_column(Integer(),nullable=False)
    error_message : Mapped[str] = mapped_column(Text(),nullable=False)
    created_at : Mapped[datetime] = mapped_column(datetime(timezone=True), nullable=False ,default = lambda : datetime.now(UTC))
    updated_at : Mapped[datetime] = mapped_column(datetime(timezone=True),nullable=False, default = lambda: datetime.now(UTC),opupdate = lambda:datetime.now(UTC))