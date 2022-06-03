"""edit post, at body and add title

Revision ID: 9581444ab0a8
Revises: 5df4b0956721
Create Date: 2022-06-03 20:48:37.031644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9581444ab0a8'
down_revision = '5df4b0956721'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    # ### end Alembic commands ###