"""empty message

Revision ID: 8c777b781ea8
Revises: 83e0a28b1430
Create Date: 2016-08-24 15:09:13.241426

"""

# revision identifiers, used by Alembic.
revision = '8c777b781ea8'
down_revision = '83e0a28b1430'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image_sizes', sa.Column('full_aspect', sa.String(), nullable=True))
    op.add_column('image_sizes', sa.Column('icon_aspect', sa.String(), nullable=True))
    op.add_column('image_sizes', sa.Column('thumbnail_aspect', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image_sizes', 'thumbnail_aspect')
    op.drop_column('image_sizes', 'icon_aspect')
    op.drop_column('image_sizes', 'full_aspect')
    ### end Alembic commands ###