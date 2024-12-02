"""Add feedback table

Revision ID: 4d5e6f7g8h9i
Revises: 3c4d5e6f7g8h
Create Date: 2024-12-01 23:55:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4d5e6f7g8h9i'
down_revision = '3c4d5e6f7g8h'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('feedback',
        sa.Column('feedback_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('feedback_uuid', mysql.CHAR(length=36), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('reservation_id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.Column('comments', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['reservation_id'], ['reservation.reservation_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('feedback_id'),
        sa.UniqueConstraint('feedback_uuid')
    )


def downgrade():
    op.drop_table('feedback')
