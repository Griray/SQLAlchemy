from sqlalchemy.orm import Query

from models import Publisher, Book, Shop, Session

if __name__ == '__main__':
    session = Session()
    publish = session.query(Publisher)
    book = session.query(Book)
    shop = session.query(Shop)
    q = Query([Publisher, Book, Shop], session=Session)

    publ1 = Publisher(id=1, name='Foma'),
    publ2 = Publisher(id=2, name='EKSMO'),
    publ3 = Publisher(id=3, name='Key'),
    publ4 = Publisher(id=4, name='Train'),

    book1 = Book(id=1, name='Dorian Grey'),
    book2 = Book(id=2, name='Harry Potter'),
    book3 = Book(id=3, name='Dream'),
    book4 = Book(id=4, name='Perfume'),
    book5 = Book(id=5, name='Night in Lisbon'),
    book6 = Book(id=6, name='3 Fellows'),
    book7 = Book(id=7, name='Post'),
    book8 = Book(id=8, name='Kingdom'),

    shop1 = Shop(id=1, name='Mir Knig'),
    shop2 = Shop(id=2, name='Dom Knigi'),
    shop3 = Shop(id=3, name='BookBerry'),

    session.add_all([publ1, publ2, publ3, publ4, book1, book2, book3, book4, book5, book6, book7, book8, shop1, shop2,
                     shop3])
    session.commit()


    ask_for_publisher = int(input('Введите Id номер издателя '))
    subq = session.query(Publisher).filter(Publisher.id == ask_for_publisher).all()

    def publisher_books():
        book_list = session.query(Book).join
