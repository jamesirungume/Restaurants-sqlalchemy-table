from sqlalchemy import create_engine,func
from sqlalchemy import ForeignKey,Column,Integer,String,DateTime,Table
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurants.db')
Base = declarative_base()

restaurant_customer = Table(
    'restaurant_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing = True,
)


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    created_at = Column(DateTime(), server_default=func.now())

    reviews = relationship('Review', backref= backref('restaurant'))
    customers = relationship('Customer',secondary = restaurant_customer, back_populates = 'restaurants')

    def __repr__(self):
        return f'Restaurant(id ={self.id}, ' + \
            f'name = {self.name },' + \
            f'created_at = {self.created_at})'
    

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    full_name = Column(String())
    favorite_restaurant =Column(String())

    reviews = relationship('Review', backref = backref('customer'))
    restaurants = relationship('Restaurant',secondary = restaurant_customer, back_populates = 'customers')

    def __repr__(self):
        return f'Customer(id = {self.id}' + \
        f'name = {self.name})'
    
    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))



    def __repr__(self):
        return f'Review(id = {self.id}' + \
        f'star_rating = {self.star_rating}' +\
        f'created_at = {self.created_at})'