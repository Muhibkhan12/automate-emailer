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
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
