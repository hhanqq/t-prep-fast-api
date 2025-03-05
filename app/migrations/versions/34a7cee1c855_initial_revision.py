"""Initial revision

Revision ID: 34a7cee1c855
Revises: 6ff648fbd7c6
Create Date: 2025-03-05 16:55:33.285583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34a7cee1c855'
down_revision: Union[str, None] = '6ff648fbd7c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Question', sa.Column('correct_answer', sa.String(), nullable=False))
    op.add_column('Question', sa.Column('wr_answer1', sa.String(), nullable=False))
    op.add_column('Question', sa.Column('wr_answer2', sa.String(), nullable=False))
    op.add_column('Question', sa.Column('wr_answer3', sa.String(), nullable=False))
    op.drop_column('Question', 'wr_answr2')
    op.drop_column('Question', 'wr_answr1')
    op.drop_column('Question', 'wr_answr3')
    op.drop_column('Question', 'correct_answr')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Question', sa.Column('correct_answr', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Question', sa.Column('wr_answr3', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Question', sa.Column('wr_answr1', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Question', sa.Column('wr_answr2', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('Question', 'wr_answer3')
    op.drop_column('Question', 'wr_answer2')
    op.drop_column('Question', 'wr_answer1')
    op.drop_column('Question', 'correct_answer')
    # ### end Alembic commands ###
