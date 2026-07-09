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
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
