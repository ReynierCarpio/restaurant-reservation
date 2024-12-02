"""Add reservation table

Revision ID: 3c4d5e6f7g8h
Revises: 2b3c4d5e6f7g
Create Date: 2024-12-01 23:50:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3c4d5e6f7g8h'
down_revision = '2b3c4d5e6f7g'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('reservation',
        sa.Column('reservation_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('reservation_uuid', mysql.CHAR(length=36), nullable=False),
        sa.Column('restaurant_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('table_id', sa.Integer(), nullable=False),
        sa.Column('reservation_date_time', sa.DateTime(), nullable=False),
        sa.Column('status', sa.Enum('Pending', 'Confirmed', 'Cancelled'), nullable=False),
        sa.Column('guests', sa.Integer(), nullable=False),
        sa.Column('special_request', sa.String(length=255), nullable=True),
        sa.Column('party_size', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.restaurant_id'], ),
        sa.ForeignKeyConstraint(['table_id'], ['table_number.table_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('reservation_id'),
        sa.UniqueConstraint('reservation_uuid')
    )


def downgrade():
    op.drop_table('reservation')
