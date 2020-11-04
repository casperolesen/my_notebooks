import sqlalchemy as s_a
from sqlalchemy import Column, Integer, String, Float, BigInteger, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import os

import json

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    Rating = Column(Float)
    Reviews = Column(Text)
    Book_title = Column(Text)
    Description = Column(Text)
    Number_Of_Pages = Column(BigInteger)
    Type = Column(Text)
    Price = Column(Float)

    def __repr__(self):
        #return f'Book {self.Book_title}'
        return {
            "id": self.id,
            "title": self.Book_title
        }
   

class TestDB():
    
    def __init__(self):
        self.engine = s_a.create_engine("mysql+mysqlconnector://root:root@db/test", echo=False)
        self.Base = Base
        self.Base.metadata.drop_all(self.engine)
        self.create_data()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_data(self):
        self.Base.metadata.create_all(self.engine)
        target_path = os.path.join(os.path.dirname(__file__), '../../files/prog_book.csv')
        df = pd.read_csv(target_path)
        df.to_sql('books', schema='test', con=self.engine, if_exists='append', index = False)
    
    def all_books(self):
        books = [book for book in self.session.query(Book).all()]
        #for book in self.session.query(Book).all():
            #print(book.items())
        
        return books

#db = TestDB(Base)
#db = TestDB()
#db.create_data()
#db.all_books()