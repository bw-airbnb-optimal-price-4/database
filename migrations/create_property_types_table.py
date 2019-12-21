from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import Table


def create_property_types_table(metadata):
    property_types = Table('property_types', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('property_type', String(255)),
                           )
    return property_types
