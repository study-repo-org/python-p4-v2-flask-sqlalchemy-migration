"""rename department

Revision ID: efc63e3ec7e2
Revises: 1a7cb1c2a3c8
Create Date: 2024-06-23 16:05:34.316375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efc63e3ec7e2'
down_revision = '1a7cb1c2a3c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###