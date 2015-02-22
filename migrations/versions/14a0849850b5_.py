"""empty message

Revision ID: 14a0849850b5
Revises: 241caef0aa3
Create Date: 2015-02-22 22:27:56.345155

"""

# revision identifiers, used by Alembic.
revision = '14a0849850b5'
down_revision = '241caef0aa3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('citations', 'date',
               existing_type=sa.DATETIME(),
               nullable=True)
    op.drop_column('citations', '_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('citations', sa.Column('_id', sa.INTEGER(), nullable=False))
    op.alter_column('citations', 'date',
               existing_type=sa.DATETIME(),
               nullable=False)
    ### end Alembic commands ###
