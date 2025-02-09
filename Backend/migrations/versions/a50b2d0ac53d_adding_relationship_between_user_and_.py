"""adding relationship between user and events models

Revision ID: a50b2d0ac53d
Revises: f5eac3d7916d
Create Date: 2025-02-10 13:18:14.129890

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a50b2d0ac53d'
down_revision = 'f5eac3d7916d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('county', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('area', sa.String(length=100), nullable=False))
        batch_op.drop_column('country')
        batch_op.drop_column('city')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', mysql.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('country', mysql.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('area')
        batch_op.drop_column('county')

    # ### end Alembic commands ###
