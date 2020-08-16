from models import Publisher, Session

if __name__ == '__main__':
    session = Session()
    publisher = Session.query(Publisher)