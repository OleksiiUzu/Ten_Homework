"""first migration

Revision ID: 4e460cd34fea
Revises: 
Create Date: 2023-08-27 10:37:33.118026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e460cd34fea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('ID')
    )
    op.create_table('Status',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('status')
    )
    op.create_table('User_type',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('Name')
    )
    op.create_table('Dishes',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Dish_name', sa.String(length=120), nullable=False),
    sa.Column('Price', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(length=256), nullable=True),
    sa.Column('Available', sa.Integer(), nullable=False),
    sa.Column('Category', sa.Integer(), nullable=False),
    sa.Column('Photo', sa.String(length=256), nullable=True),
    sa.Column('Ccal', sa.Integer(), nullable=False),
    sa.Column('Protein', sa.Integer(), nullable=False),
    sa.Column('Fat', sa.Integer(), nullable=False),
    sa.Column('Carb', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Category'], ['Category.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('ID')
    )
    op.create_table('User',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Telephone', sa.Integer(), nullable=False),
    sa.Column('Email', sa.String(length=120), nullable=False),
    sa.Column('Password', sa.String(length=50), nullable=False),
    sa.Column('Tg', sa.String(length=120), nullable=True),
    sa.Column('Type', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Type'], ['User_type.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('Telephone'),
    sa.UniqueConstraint('Tg')
    )
    op.create_table('Address',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Town', sa.String(length=120), nullable=False),
    sa.Column('Street', sa.String(length=120), nullable=False),
    sa.Column('House', sa.String(length=120), nullable=False),
    sa.Column('Apt', sa.String(length=120), nullable=True),
    sa.Column('Block', sa.Integer(), nullable=True),
    sa.Column('Floor', sa.Integer(), nullable=True),
    sa.Column('User', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['User'], ['User.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('ID')
    )
    op.create_table('Dish_rate',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Dish', sa.Integer(), nullable=False),
    sa.Column('User', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Dish'], ['Dishes.ID'], ),
    sa.ForeignKeyConstraint(['User'], ['User.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('Dish'),
    sa.UniqueConstraint('ID'),
    sa.UniqueConstraint('User')
    )
    op.create_table('Orders',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('User', sa.Integer(), nullable=False),
    sa.Column('Address', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('Ccal', sa.Integer(), nullable=False),
    sa.Column('Fat', sa.Integer(), nullable=False),
    sa.Column('Protein', sa.Integer(), nullable=False),
    sa.Column('Carbon', sa.Integer(), nullable=False),
    sa.Column('Coment', sa.Integer(), nullable=True),
    sa.Column('Order_date', sa.Integer(), nullable=False),
    sa.Column('Rate', sa.Integer(), nullable=True),
    sa.Column('Status', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['Address'], ['Address.ID'], ),
    sa.ForeignKeyConstraint(['Status'], ['Status.ID'], ),
    sa.ForeignKeyConstraint(['User'], ['User.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('ID'),
    sa.UniqueConstraint('Status')
    )
    op.create_table('Ordered_dishes',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('dish', sa.String(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dish'], ['Dishes.ID'], ),
    sa.ForeignKeyConstraint(['order_id'], ['Orders.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Ordered_dishes')
    op.drop_table('Orders')
    op.drop_table('Dish_rate')
    op.drop_table('Address')
    op.drop_table('User')
    op.drop_table('Dishes')
    op.drop_table('User_type')
    op.drop_table('Status')
    op.drop_table('Category')
    # ### end Alembic commands ###