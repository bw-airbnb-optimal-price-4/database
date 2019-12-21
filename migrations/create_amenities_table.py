from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import Table


def create_amenities_table(metadata):
    amenities = Table('amenities', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('amenity', String(255), nullable=False)
                      )

    return amenities
