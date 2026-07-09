""" create campaign reciptents table

Revision ID: 5e8f0cc6c5d3
Revises: cb15a195f3a6
Create Date: 2026-07-09 20:22:46.733558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e8f0cc6c5d3'
down_revision: Union[str, Sequence[str], None] = 'cb15a195f3a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('campaigns_recipitents',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('campaign_id',sa.Integer(), sa.ForeignKey(
            'campaigns.id',
            ondelete='CASCADE',
        )),
        sa.Column('sender_account_id',sa.Integer(), sa.ForeignKey(
            'sender_account.id',
            ondelete='CASCADE',
        )),
        sa.Column('recipitent_name',sa.String(255),nullable=True),
        sa.Column('recipitent_email',sa.String(255),nullable=True),
        sa.Column('company',sa.String(255),nullable=True),
        sa.Column('phone',sa.String(100),nullable=False),
        sa.Column('status',sa.Enum('pending','sending','sent','Failed')),
        sa.Column('retry_count',sa.Integer()),
        sa.Column('error_message',sa.text()),
        sa.Column('created_at',sa.Datetime(),nullable=True),
        sa.Column('updated_at',sa.Datetime(),nullable=True)
    
    )


def downgrade() -> None:
    op.drop_table('campaings_recipitent')
