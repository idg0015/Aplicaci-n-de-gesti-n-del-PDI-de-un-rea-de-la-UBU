"""Cambio de nombre columna query

Revision ID: 84794a0ff805
Revises: 5d06c4989a14
Create Date: 2023-06-06 11:23:47.887741

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '84794a0ff805'
down_revision = '5d06c4989a14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('docente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('read', sa.Boolean(), nullable=False))
        batch_op.drop_column('query')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('docente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('query', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
        batch_op.drop_column('read')

    # ### end Alembic commands ###
