"""Renaming students to scholars

Revision ID: e1d9b2c2a5ca
Revises: 791279dd0760
Create Date: 2024-03-25 12:26:19.594433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1d9b2c2a5ca'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
