from sqlalchemy import create_engine,func
from sqlalchemy import ForeignKey,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurants.db')
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    created_at = Column(DateTime(), server_default=func.now())

    def __repr__(self):
        return f'Restaurant(id ={self.id}, ' + \
            f'name = {self.name },' + \
            f'created_at = {self.created_at})'
    
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(integer(), primary_key=True)
    name = Column(string())

    def __repr__(self):
        return f'Customer(id = {self.id}' + \
        f'name = {self.name})'
    
class Review(Base):
    __tablename__ = 'reviews'
    id = column(Integer(), primary_key=True)
    star_rating = Column(Integer())

    def __repr__(self):
        return f'Review(id = {self.id}' + \
        f'star_rating = {self.star_rating})'