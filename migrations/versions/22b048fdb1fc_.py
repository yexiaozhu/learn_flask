"""empty message

Revision ID: 22b048fdb1fc
Revises: e084049c8ddf
Create Date: 2016-11-18 01:23:18.711454

"""

# revision identifiers, used by Alembic.
revision = '22b048fdb1fc'
down_revision = 'e084049c8ddf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
