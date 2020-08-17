import sqlalchemy as sq
from sqlalchemy import sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2

engine = sq.create_engine('postgresql+psycopg2://postgres:postgres@localhost:5439//Alchemy')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.Integer)


sale_stock = sq.Table('sale_stock', Base.metadata,
                      sq.Column('sale_id', sq.Integer, sq.ForeignKey('Sale.id')),
                      sq.Column('stock_id', sq.Integer, sq.ForeignKey('Stock.id'))
                      )


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    id_stock = relationship('stock', secondary=sale_stock, back_populates='stocks')
    count = sq.Column(sq.Integer)
