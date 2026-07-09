"""creating tempaltes table

Revision ID: cb15a195f3a6
Revises: 32dabc00837f
Create Date: 2026-07-09 20:08:23.884260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb15a195f3a6'
down_revision: Union[str, Sequence[str], None] = '32dabc00837f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('templates',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('user_id',sa.Integer(),sa.ForeignKey(
            'users.id',
            ondelete='CASCADE',
        )),
        sa.Column('template_id',sa.Integer(),sa.ForeignKey(
            'templates.id',
            ondelete='CASCADE',
        )),
        sa.Column('subject',sa.String(255),nullable=False),
        sa.Column('html_body',sa.text(),nullable=False),
        sa.Column('created_at',sa.Datetime(),nullable=False),
        sa.Column('updated_at',sa.Datetime(),nullable=False),
    )


def downgrade() -> None:
    op.drop_table('templates')