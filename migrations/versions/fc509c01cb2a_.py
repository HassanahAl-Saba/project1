"""empty message

Revision ID: fc509c01cb2a
Revises: 31cae8c59eda
Create Date: 2021-03-23 23:22:36.088063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc509c01cb2a'
down_revision = '31cae8c59eda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('type', sa.String(length=20), nullable=True))
    op.drop_column('properties', 'property_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('property_type', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('properties', 'type')
    # ### end Alembic commands ###