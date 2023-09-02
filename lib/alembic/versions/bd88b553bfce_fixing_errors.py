"""fixing errors

Revision ID: bd88b553bfce
Revises: 2c3f895a84cd
Create Date: 2023-09-02 16:56:26.535880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd88b553bfce'
down_revision: Union[str, None] = '2c3f895a84cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_customers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_customers',
    sa.Column('restaurant_id', sa.INTEGER(), nullable=False),
    sa.Column('customer_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('restaurant_id', 'customer_id')
    )
    # ### end Alembic commands ###
