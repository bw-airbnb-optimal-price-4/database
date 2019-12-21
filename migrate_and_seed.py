import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

from migrations import create_users_table, create_listing_amenities_table, \
    create_listings_table, create_amenities_table, \
    create_property_types_table, create_neighborhoods_table
from seeds import property_types_seed, amenities_seed, neighborhoods_seed

load_dotenv()

if __name__ == '__main__':
    engine = create_engine(os.getenv("DATABASE_URL"))
    metadata = MetaData()

    amenities_table = create_amenities_table(metadata)
    property_types_table = create_property_types_table(metadata)
    neighborhoods_table = create_neighborhoods_table(metadata)
    users_table = create_users_table(metadata)
    listings_table = create_listings_table(metadata)
    listing_amenities_table = create_listing_amenities_table(metadata)

    metadata.create_all(engine)

    with engine.connect() as c:
        c.execute(amenities_table.insert().values(amenities_seed))
        c.execute(neighborhoods_table.insert().values(neighborhoods_seed))
        c.execute(property_types_table.insert().values(property_types_seed))
