from sqlalchemy.orm import Query

from models import Stock, Book, Publisher, Shop, Session

ask_input = int(input('Введите ID номер издателя '))
if __name__ == '__main__':
    session = Session()
    q = Query([Stock, Book, Publisher, Shop])
    publ_book = session.query(Book).filter(Book.id_publisher == ask_input).subquery()
    join_proc = session.query(publ_book).join(Stock.id_book)
    shop_list_join = session.query(join_proc).join(Shop.id)
    shop_list = session.query(Shop.id).all()
    print(shop_list)
