"""empty message

Revision ID: 355f9336615a
Revises: 5b45e82ebce3
Create Date: 2017-08-23 21:02:05.782000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '355f9336615a'
down_revision = '5b45e82ebce3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
