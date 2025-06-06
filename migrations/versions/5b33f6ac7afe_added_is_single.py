"""added is_single

Revision ID: 5b33f6ac7afe
Revises: 5545f5a3afb3
Create Date: 2025-04-20 23:21:02.180809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b33f6ac7afe'
down_revision: Union[str, None] = '5545f5a3afb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('albums', sa.Column('is_single', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('albums', 'is_single')
    # ### end Alembic commands ###
