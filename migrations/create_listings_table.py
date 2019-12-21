from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Float, SmallInteger
from sqlalchemy import Table
from sqlalchemy.dialects.postgresql import ENUM


def create_listings_table(metadata):
    room_types_enum = ENUM('Entire Home/Apt', 'Private Room', 'Shared Room',
                           'Hotel Room', name='room_types', metadata=metadata)
    listings = Table('listings', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('user_id', Integer, ForeignKey("users.id"),
                            nullable=False),
                     Column('property_type_id', Integer,
                            ForeignKey("property_types.id"), nullable=False),
                     Column('neighborhood_id', Integer,
                            ForeignKey("neighborhoods.id"), nullable=False),
                     Column('room_type', room_types_enum, nullable=False),
                     Column('accommodates', Integer, nullable=False),
                     Column('bedrooms', Integer, nullable=False),
                     Column('bathrooms', Integer, nullable=False),
                     Column('beds', Integer, nullable=False),
                     Column('listing_url', String(355), nullable=False),
                     Column('title', String(255), nullable=False),
                     Column('picture_url', String(355)),
                     Column('city', String(255), nullable=False),
                     Column('state', String(2), nullable=False),
                     Column('zip', SmallInteger, nullable=False),
                     Column('country', String(255), nullable=False),
                     Column('latitude', Float, nullable=False),
                     Column('longitude', Float, nullable=False)
                     )

    return listings
