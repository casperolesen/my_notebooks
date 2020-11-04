import sqlalchemy as s_a
from sqlalchemy import Column, Integer, String, Float, BigInteger, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

import sys
import os

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
        return f'User {self.name}'

class BookDB():
    
    def __init__(self):
        self.engine = s_a.create_engine("mysql+mysqlconnector://root:root@db")

    def createDatabase(self):
        self.engine.execute("DROP DATABASE IF EXISTS week8")
        self.engine.execute("CREATE DATABASE IF NOT EXISTS week8")
        
        # load data to panda dataframe
        #print(filepath)
        print(os.getcwd())
        print(os.path.dirname(__file__))
        #print(__file__)
        target_path = os.path.join(os.path.dirname(__file__), '../../files/prog_book.csv')
        
        print(target_path)
        print(os.path.normpath(target_path))
        df = pd.read_csv(target_path)
        df.to_sql('books', schema='week8', con=self.engine, if_exists='replace', index = False)

        #self.engine.execute("USE week8")

    def all_books(self):
        ResultProxy = self.engine.execute("SELECT * FROM week8.books")
        ResultSet = ResultProxy.fetchall()
        items = [dict(row.items()) for row in ResultSet]
        return items

    def best_books(self):
        ResultProxy = self.engine.execute("SELECT * FROM week8.books ORDER BY Rating DESC LIMIT 10")
        ResultSet = ResultProxy.fetchall()
        items = [dict(row.items()) for row in ResultSet]
        return items

    def create_book(self, book):
        df = pd.DataFrame(book, index=[0])
        df.to_sql('books', schema='week8', con=self.engine, if_exists='append', index = False)

        q = "SELECT * FROM week8.books WHERE Book_title = '{}'".format(book['Book_title'])
        ResultProxy = self.engine.execute(q)
        ResultSet = ResultProxy.fetchall()
        items = [dict(row.items()) for row in ResultSet]
        return items


    def delete_book(self, title):
        try:
            self.engine.execute("DELETE FROM week8.books WHERE Book_title = '{}'".format(title))
            return True
        except expression as identifier:
            return False

    def edit_book(self):
        pass

    def avg_price(self):
        pass