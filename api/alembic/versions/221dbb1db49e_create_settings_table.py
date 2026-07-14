"""create settings  table

Revision ID: 221dbb1db49e
Revises: 7104c7c4b156
Create Date: 2026-07-09 21:11:53.467668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '221dbb1db49e'
down_revision: Union[str, Sequence[str], None] = '7104c7c4b156'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'settings',
        sa.Column('id',sa.Integer(),primary_key=True,nullable=False),
        sa.Column('company_name',sa.String(255),nullable=False),
        sa.Column('timezone',sa.DateTime(),nullable=False),
        sa.Column('default_sender_account_id',sa.Integer(),sa.ForeignKey(
            'sender_accounts.id',
            ondelete='CASCADE',
        )),
        sa.Column('created_at',sa.DateTime(),nullable=True),
        sa.Column('updated_at',sa.DateTime(),nullable=True),
    )

def downgrade() -> None:
    op.drop_table('settings')
