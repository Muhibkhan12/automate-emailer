"""create email_logs table

Revision ID: 355b391c978e
Revises: 5e8f0cc6c5d3
Create Date: 2026-07-09 21:11:12.184386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '355b391c978e'
down_revision: Union[str, Sequence[str], None] = '5e8f0cc6c5d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('email_logs',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('campaign_recipitent_id',sa.Integer(),sa.ForeignKey(
            'campaign_recipients.id',
            ondelete='CASCADE',
        )),
        sa.Column('sender_account_id',sa.Integer(),sa.ForeignKey(
            'sender_accounts.id',
            ondelete='CASCADE'
        )),
        sa.Column('action',sa.String(200),nullable=False),
        sa.Column('message',sa.Text(),nullable=False),
        sa.Column('created_at',sa.String(255),nullable=False),

    )

def downgrade() -> None:
    """Downgrade schema."""
    pass
