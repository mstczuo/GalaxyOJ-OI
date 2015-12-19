"""empty message

Revision ID: 68e8dc54baaf
Revises: None
Create Date: 2015-12-20 00:20:12.053168

"""

# revision identifiers, used by Alembic.
revision = '68e8dc54baaf'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('privilege_level', sa.Integer(), nullable=False),
    sa.Column('login_name', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('nickname', sa.String(length=32), nullable=True),
    sa.Column('signature', sa.String(length=128), nullable=True),
    sa.Column('real_name', sa.String(length=32), nullable=True),
    sa.Column('note', sa.String(length=256), nullable=True),
    sa.Column('password_hash', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login_name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
