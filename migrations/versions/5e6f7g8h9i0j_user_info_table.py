"""Add user_info table

Revision ID: 5e6f7g8h9i0j
Revises: 4d5e6f7g8h9i
Create Date: 2024-12-01 23:58:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e6f7g8h9i0j'
down_revision = '4d5e6f7g8h9i'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_info',
        sa.Column('user_info_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_info_uuid', mysql.CHAR(length=36), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('reservation_id', sa.Integer(), nullable=False),
        sa.Column('reference_no', sa.String(length=255), nullable=False),
        sa.Column('mode_of_payment', sa.Enum('Cash', 'Card', 'Online'), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['reservation_id'], ['reservation.reservation_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('user_info_id'),
        sa.UniqueConstraint('user_info_uuid')
    )


def downgrade():
    op.drop_table('user_info')
