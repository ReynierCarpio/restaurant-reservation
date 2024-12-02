"""Add restaurant table

Revision ID: 1a2b3c4d5e6f
Revises: 5f872e0a365a
Create Date: 2024-12-01 23:40:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1a2b3c4d5e6f'
down_revision = '5f872e0a365a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('restaurant',
        sa.Column('restaurant_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('restaurant_uuid', mysql.CHAR(length=36), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('address', sa.String(length=255), nullable=False),
        sa.Column('contact_number', sa.Integer(), nullable=False),
        sa.Column('business_hours', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('restaurant_id'),
        sa.UniqueConstraint('restaurant_uuid')
    )


def downgrade():
    op.drop_table('restaurant')
