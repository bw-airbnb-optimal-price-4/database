from sqlalchemy import Column
from sqlalchemy import Integer, String, Date
from sqlalchemy import Table


def create_users_table(metadata):
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('email', String(355), nullable=False),
                  Column('first_name', String(60), nullable=False),
                  Column('last_name', String(60), nullable=False),
                  Column('city', String(255)),
                  Column('state', String(2)),
                  Column('date_of_birth', Date),
                  Column('profile_image_id', Integer)
                  )
    return users
