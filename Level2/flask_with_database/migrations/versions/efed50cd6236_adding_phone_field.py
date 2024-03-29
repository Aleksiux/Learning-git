"""adding phone field

Revision ID: efed50cd6236
Revises: 5fda51c45f29
Create Date: 2023-02-21 20:49:18.777408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efed50cd6236'
down_revision = '5fda51c45f29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['phone'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('phone')

    # ### end Alembic commands ###
