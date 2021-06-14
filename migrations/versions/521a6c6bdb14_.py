"""empty message

Revision ID: 521a6c6bdb14
Revises: 
Create Date: 2021-06-12 15:29:16.579354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '521a6c6bdb14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.Column('city', sa.String(length=150), nullable=True),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('zip', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('location_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=150), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location_status')
    op.drop_table('user')
    op.drop_table('location')
    # ### end Alembic commands ###