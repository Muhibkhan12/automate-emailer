"""create sender_accounts

Revision ID: 32dabc00837f
Revises: f80696be8edb
Create Date: 2026-07-09 19:44:00.759721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32dabc00837f'
down_revision: Union[str, Sequence[str], None] = 'f80696be8edb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("sender_account",
    sa.Column('id',sa.Integer(255),nullable=False),
    sa.Column('email',sa.String(255),Unique=True),
    sa.Column('display_name',sa.String(255),nullable=False),
    sa.Column('smtp_host',sa.String(255),nullable=False),
    sa.Column('smtp_port',sa.Integer(),nullable=False),
    sa.Column('username',sa.String(255),nullable=False),
    sa.Column('password',sa.text(),nullable=False),
    sa.Column('daily_limit',sa.Integer(),nullable=False),
    sa.Column('hourly_limit',sa.Integer(),nullable=False),
    sa.Column('emails_sent_today',sa.Integer(),nullable=False),
    sa.Column('emails_sent_hour',sa.Integer(),nullable=False),
    sa.Column('status',sa.Enum("active","unactive",nullable=False)),
    sa.Column('created_at',sa.Datetime()),
    sa.Column('updated_at',sa.Datetime()),
    )


def downgrade() -> None:
    op.drop_table('sender_account')