"""delete cascade dataset

Revision ID: 385fd5385e36
Revises: 35c85c5bfcb2
Create Date: 2013-05-22 14:25:07.869066

"""

# revision identifiers, used by Alembic.
revision = '385fd5385e36'
down_revision = '35c85c5bfcb2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("resource_dataset_id_fkey", "resource", type='foreignkey')
    op.create_foreign_key(
        "resource_dataset_id_fkey",
        "resource",
        "dataset",
        ["dataset_id"],
        ["name"],
        ondelete="CASCADE"
    )

    op.drop_constraint("activity_resource_url_fkey", "activity", type='foreignkey')
    op.create_foreign_key(
        "activity_resource_url_fkey",
        "activity",
        "resource",
        ["resource_url"],
        ["url"],
        ondelete="CASCADE"
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("resource_dataset_id_fkey", "resource", type='foreignkey')
    op.create_foreign_key(
        "resource_dataset_id_fkey",
        "resource",
        "dataset",
        ["dataset_id"],
        ["name"],
    )

    op.drop_constraint("activity_resource_url_fkey", "activity", type='foreignkey')
    op.create_foreign_key(
        "activity_resource_url_fkey",
        "activity",
        "resource",
        ["resource_url"],
        ["url"],
    )
    ### end Alembic commands ###