from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://sharma1:sharma95@localhost:5432/db_assignment', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#defining the schema
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    author_id = Column(Integer(), ForeignKey('authors.id'))


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))

    books = relationship('Book', backref='author')

Base.metadata.create_all(engine)


#-Inserting Data-

# author1 = Author(firstname="Jen", lastname="Beagin")
# author2 = Author(firstname="Alex", lastname="Dunne")

# book1 = Book(title="Big Swiss", description="Do you love darkly humorous novels with messy protagonists making questionable decisions? Then this is the book for you!", author=author1)

# session.add(book1)
# session.commit()

# print(book1.title)
# print(book1.id)

# book2 = Book(title="Pretend I'm Dead", description="Pretend I'm Dead is the first novel published by writer Jen Beagin. It was followed by a sequel novel titled Vacuum in the Dark. Pretend I'm Dead was shortlisted for The Center for Fiction's 2018 First Novel Prize.", author=author1)

# book3 = Book(title="The Book Of Secrets", description="When fairies return to a small Irish village, they bring with them something else, something sinister. Now, a group of friends must work together to stop their home from being destroyed.", author=author2)

# session.add_all([book2, book3])
# session.flush()

#Querying data
books = session.query(Book).all()
for book in books:
    print(book.id, book.title, book.description)

#-Updating data in tables-
# book = session.query(Book).filter(Book.id=="12").first()
# book.title = "Duplicate Big Swiss"
# session.commit()
# print(book.book_name)


#-Deleting data-
# book = session.query(Book).filter(Book.id=="12").first()
# session.delete(book)
# session.commit()
# print(book.book_name)


