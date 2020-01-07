from sqlalchemy import Column
from sqlalchemy import Integer, String, Date, SmallInteger
from sqlalchemy import Table


def create_users_table(metadata):
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('email', String(255), nullable=False),
                  Column('password', String(60), nullable=False),
                  Column('first_name', String(225)),
                  Column('last_name', String(255)),
                  Column('city', String(255)),
                  Column('zip_code', SmallInteger),
                  Column('state', String(2)),
                  Column('date_of_birth', Date),
                  Column('profile_image', String(255))
                  )
    return users
