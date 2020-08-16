import sqlalchemy as sq
from sqlalchemy import sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = sq.create_engine('')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
Base = declarative_base()

publisher_book = sq.Table('publisher_book', Base.metadata,
                          sq.Column('publisher_id', sq.Integer, sq.ForeignKey('Publisher.id')),
                          sq.Column('book_id', sq.Integer, sq.ForeignKey('Book.id'))
                          )


class Publisher(Base):
    __tablename__ = 'Publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)


book_stock = sq.Table('book_stock', Base.metadata,
                      sq.Column('book_id', sq.Integer, sq.ForeignKey('Book.id')),
                      sq.Column('stock_id', sq.Integer, sq.ForeignKey('Stock.id'))
                      )

stock_shop = sq.Table('stock_shop', Base.metadata,
                      sq.Column('stock_id', sq.Integer, sq.ForeignKey('Stock.id')),
                      sq.Column('shop_id', sq.Integer, sq.ForeignKey('Shop.id'))
                      )


class Book(Base):
    __tablename__ = 'Book'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    id_publisher = relationship('Publisher', secondary=publisher_book, back_populates='publishers')


class Shop(Base):
    __tablename__ = 'Shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)


class Stock(Base):
    __tablename__ = 'Stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = relationship('Book', secondary=book_stock, back_populates='books')
    id_shop = relationship('Shop', secondary=stock_shop, back_populates='shops')
    count = sq.Column(sq.Integer)


sale_stock = sq.Table('sale_stock', Base.metadata,
                      sq.Column('sale_id', sq.Integer, sq.ForeignKey('Sale.id')),
                      sq.Column('stock_id', sq.Integer, sq.ForeignKey('Stock.id'))
                      )


class Sale(Base):
    __tablename__ = 'Sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    id_stock = relationship('Stock', secondary=sale_stock, back_populates='stocks')
    count = sq.Column(sq.Integer)
