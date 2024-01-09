"""empty message

Revision ID: ca12d53bf0da
Revises: 48a3abaa4bfd
Create Date: 2024-01-08 08:53:22.869156

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca12d53bf0da'
down_revision = '48a3abaa4bfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('transaction_type',
               existing_type=mysql.ENUM('BALANCE_ADDITION', 'PURCHASE'),
               type_=sa.Enum('BALANCE', 'PURCHASE', name='transactiontype'),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.alter_column('transaction_type',
               existing_type=sa.Enum('BALANCE', 'PURCHASE', name='transactiontype'),
               type_=mysql.ENUM('BALANCE_ADDITION', 'PURCHASE'),
               existing_nullable=False)

    # ### end Alembic commands ###
