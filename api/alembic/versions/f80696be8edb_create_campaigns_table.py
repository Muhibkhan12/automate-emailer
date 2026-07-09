"""create emailing table

Revision ID: f80696be8edb
Revises: 3c39bf5702ae
Create Date: 2026-07-09 19:12:11.250899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f80696be8edb'
down_revision: Union[str, Sequence[str], None] = '3c39bf5702ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'campaigns',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('user_id',sa.Integer(),sa.ForeignKey(
            "users.id",
            ondelete="CASCADE",
        )),
        sa.Column('template_id',sa.Integer(),sa.ForeignKey(
            "templates.id",
            ondelete='CASCADE'
        )),
        sa.Column('name',sa.String(255),nullable=False),
        sa.Column('status',sa.Enum(
            "Pending",
            "Running",
            "Paused",
            "Completed",
            "Cancelled",
            name="campaing_status"
        ),
        nullable=False,
        server_default="Pending"
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
        )
    )


def downgrade() -> None:
    op.drop_table('campaigns')