"""add users table

Revision ID: 0994f987cbbe
Revises: af427bd03f14
Create Date: 2022-02-08 13:27:35.710841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0994f987cbbe'
down_revision = 'af427bd03f14'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
