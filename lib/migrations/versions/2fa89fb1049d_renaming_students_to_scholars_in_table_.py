"""Renaming grade to level

Revision ID: 2fa89fb1049d
Revises: e1d9b2c2a5ca
Create Date: 2024-03-25 12:34:35.292574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fa89fb1049d'
down_revision = 'e1d9b2c2a5ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'grade', new_column_name='level')
    
def downgrade() -> None:
    op.alter_column('scholars', 'level', new_column_name='grade')
