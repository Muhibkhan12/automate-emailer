"""create users table

Revision ID: 3c39bf5702ae
Revises: 
Create Date: 2026-07-06 21:17:40.119508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c39bf5702ae'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id',sa.Integer(),primary_key=True),
        sa.Column('name',sa.String(255),nullable=True),
        sa.Column('email',sa.String(255),unique=True),
        sa.Column('password',sa.String(255),nullable=False),
        sa.Column('email_verification',sa.Boolean(),nullable=False,server_default="0"),
        sa.Column('verification_token',sa.String(255),nullable=True),
        sa.Column('jwt_token',sa.String(500),nullable=True),
        sa.Column('created_at',sa.DateTime(),nullable=False),
        sa.Column('updated_at',sa.DateTime(),nullable=False),
        )


def downgrade() -> None:
    op.drop_table("users")
