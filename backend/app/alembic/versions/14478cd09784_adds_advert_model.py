"""Adds advert model

Revision ID: 14478cd09784
Revises: d4867f3a4c0a
Create Date: 2021-02-07 20:07:12.743217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14478cd09784'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advert',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('inactive', sa.Boolean(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_advert_description'), 'advert', ['description'], unique=False)
    op.create_index(op.f('ix_advert_id'), 'advert', ['id'], unique=False)
    op.create_index(op.f('ix_advert_title'), 'advert', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_advert_title'), table_name='advert')
    op.drop_index(op.f('ix_advert_id'), table_name='advert')
    op.drop_index(op.f('ix_advert_description'), table_name='advert')
    op.drop_table('advert')
    # ### end Alembic commands ###