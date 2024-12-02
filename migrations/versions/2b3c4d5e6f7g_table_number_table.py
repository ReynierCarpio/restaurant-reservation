"""Add table_number table

Revision ID: 2b3c4d5e6f7g
Revises: 1a2b3c4d5e6f
Create Date: 2024-12-01 23:45:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2b3c4d5e6f7g'
down_revision = '1a2b3c4d5e6f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('table_number',
        sa.Column('table_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('table_uuid', mysql.CHAR(length=36), nullable=False),
        sa.Column('table_number', sa.String(length=50), nullable=False),
        sa.Column('restaurant_id', sa.Integer(), nullable=False),
        sa.Column('status', sa.Enum('Available', 'Reserved', 'Occupied'), nullable=False),
        sa.Column('seat', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.restaurant_id'], ),
        sa.PrimaryKeyConstraint('table_id'),
        sa.UniqueConstraint('table_uuid')
    )


def downgrade():
    op.drop_table('table_number')
