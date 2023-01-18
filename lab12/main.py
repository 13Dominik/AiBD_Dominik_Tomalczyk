from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, Text
from sqlalchemy import ForeignKey

db_string = "postgresql://postgres:postgres@localhost:5432/aibd_12"

engine = create_engine(db_string)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))

    def __repr__(self):
        return f"<users(id={self.id}, email={self.email})>"


class Host(Base):
    __tablename__ = "hosts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<hosts(id={self.id}, user_id={self.user_id})>"


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    place_id = Column(Integer, ForeignKey('places.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    price_per_night = Column(Float)
    num_nights = Column(Integer)


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    country_id = Column(Integer, ForeignKey('countries.id'))


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    rating = Column(Integer)
    review_body = Column(String(150))


class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('hosts.id'))
    address = Column(String(50))
    city_id = Column(Integer, ForeignKey('cities.id'))


class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    coutry_code = Column(String(50))
    name = Column(String(50))


Base.metadata.create_all(engine)