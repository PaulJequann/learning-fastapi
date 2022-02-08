"""add last columns to posts table

Revision ID: 895c7d8ec6ad
Revises: c8fedb11fbdc
Create Date: 2022-02-08 13:42:00.760986

"""
from time import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '895c7d8ec6ad'
down_revision = 'c8fedb11fbdc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
