"""create uploads table

Revision ID: 7104c7c4b156
Revises: 355b391c978e
Create Date: 2026-07-09 21:11:27.578693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7104c7c4b156'
down_revision: Union[str, Sequence[str], None] = '355b391c978e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('uploads',
        sa.Column('id',sa.Integer(),primary_key=True,nullable=False),
        sa.Column('campaign_id',sa.Integer(),sa.ForeignKey(
            'campaigns.id',
            ondelete='CASCADE',
        )),
        sa.Column('filename',sa.String(255),nullable=False),
        sa.Column('file_path',sa.String(255),nullable=False),
        sa.Column('total_rows',sa.Integer(),nullable=False),
        sa.Column('imported_rows',sa.Integer(),nullable=False),
        sa.Column('created_at',sa.DateTime(),nullable=True)
    )


def downgrade() -> None:
    op.drop_table('uploads')
