from sqlalchemy.orm import Query

from models import Publisher, Book, Shop, Session

Session

if __name__ == '__main__':
    session = Session()
    publish = session.query(Publisher)
    book = session.query(Book)
    shop = session.query(Shop)
    q = Query([Publisher, Book, Shop], session=Session)


    publ1 = Publisher(name='Foma'),
    publ2 = Publisher(name='EKSMO'),
    publ3 = Publisher(name='Key'),
    publ4 = Publisher(name='Train'),

    book1 = Book(name='Dorian Grey'),
    book2 = Book(name='Harry Potter'),
    book3 = Book(name='Dream'),
    book4 = Book(name='Perfume'),
    book5 = Book(name='Night in Lisbon'),
    book6 = Book(name='3 Fellows'),
    book7 = Book(name='Post'),
    book8 = Book(name='Kingdom'),

    shop1 = Shop(name='Mir Knig'),
    shop2 = Shop(name='Dom Knigi'),
    shop3 = Shop(name='BookBerry'),

    session.add_all([publ1, publ2, publ3, publ4, book1, book2, book3, book4, book5, book6, book7, book8, shop1, shop2,
                     shop3])

    

