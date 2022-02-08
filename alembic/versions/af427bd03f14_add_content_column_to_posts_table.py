"""add content column to posts table

Revision ID: af427bd03f14
Revises: 1d7da2f9dc84
Create Date: 2022-02-08 13:15:13.060589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af427bd03f14'
down_revision = '1d7da2f9dc84'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
