"""empty message

Revision ID: fe608e60fa49
Revises: 68e00ff3b382
Create Date: 2023-10-30 11:58:49.637304

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fe608e60fa49'
down_revision = '68e00ff3b382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('regular_price',
               existing_type=mysql.DECIMAL(precision=10, scale=0),
               type_=sa.Float(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('regular_price',
               existing_type=sa.Float(),
               type_=mysql.DECIMAL(precision=10, scale=0),
               existing_nullable=False)

    # ### end Alembic commands ###