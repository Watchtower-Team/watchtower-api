"""update_user_info

Revision ID: 7c759e8cd5a3
Revises: 
Create Date: 2020-07-25 00:47:44.149252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c759e8cd5a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firebase_uid', sa.String(length=128), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('user_roles', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###