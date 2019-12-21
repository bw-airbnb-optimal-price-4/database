from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import Table


def create_neighborhoods_table(metadata):
    neighborhoods = Table('neighborhoods', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('neighborhood', String(255)),
                          )
    return neighborhoods
