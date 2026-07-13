from sqlalchemy import String,Boolean,DateTime,Text,text,ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from datetime import datetime,UTC
from cors.db import Base

class EmailLogs(Base):
    __tablename__ = "email_logs"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    campaign_recipients_id: Mapped[int] = mapped_column(
    ForeignKey("campaign_recipients.id"),
    nullable=False
)
    sender_account_id: Mapped[int] = mapped_column(
    ForeignKey("sender_accounts.id"),
    nullable=False
)
    action : Mapped[str] = mapped_column(String(200),nullable=False)
    message : Mapped[str] = mapped_column(String(1000), nullable=False)
    created_at : Mapped[datetime] = mapped_column(datetime(timezone=True),nullable=False,default=lambda: datetime.now(UTC))
    updated_at : Mapped[datetime] = mapped_column(datetime(timezone=True),nullable=False, default=lambda: datetime.now(UTC),onupdate=lambda: datetime.now(UTC))

    campaign_recipients_id : Mapped["CampaignsRecipitent"] = relationship(
        back_populates="email_logs"
    )
    sender_account : Mapped["SenderAccount"] = relationship(
        back_populates="email_logs"
    )