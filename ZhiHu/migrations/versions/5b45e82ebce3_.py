"""empty message

Revision ID: 5b45e82ebce3
Revises: 7ae7d8422910
Create Date: 2017-08-23 15:32:50.317000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b45e82ebce3'
down_revision = '7ae7d8422910'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'create_time')
    # ### end Alembic commands ###