from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
location = Table('location', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('device_id', VARCHAR(length=24)),
    Column('name', VARCHAR(length=64)),
    Column('address', VARCHAR(length=80)),
    Column('latitude', FLOAT),
    Column('longitude', FLOAT),
    Column('occupancy_count', INTEGER),
    Column('last_updated', DATETIME),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['location'].columns['last_updated'].drop()
    pre_meta.tables['location'].columns['latitude'].drop()
    pre_meta.tables['location'].columns['longitude'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['location'].columns['last_updated'].create()
    pre_meta.tables['location'].columns['latitude'].create()
    pre_meta.tables['location'].columns['longitude'].create()
