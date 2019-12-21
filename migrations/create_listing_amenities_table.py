from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Table


def create_listing_amenities_table(metadata):
    listing_amenities = Table('listing_amenities', metadata,
                              Column('listing_id', Integer,
                                     ForeignKey("property_types.id"),
                                     nullable=False),
                              Column('amenities_id', Integer,
                                     ForeignKey("amenities.id"),
                                     nullable=False)
                              )
    return listing_amenities
