import sqlalchemy as s_a
from sqlalchemy import Column, Integer, String, Float, BigInteger, Text
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import os

import json

Base = declarative_base()

'''

Starting mysql server in docker:

winpty docker exec -it mysql_notebooks bash
or
docker exec -it mysql_notebooks bash

then:
mysql -u root -proot

'''

class Groceries(Base):
    __tablename__ = 'groceries'

    id = Column(Integer, primary_key=True)
    Member_number = Column(Integer)
    Date = Column(Text)
    itemDescription = Column(Text)

    def to_json(self):
        return {
            "id": self.id,
            "Member_number": self.Member_number,
            "Date": self.Date,
            "itemDescription": self.itemDescription
        }


class GroceriesDB():
    def __init__(self):
        self.engine = s_a.create_engine("mysql+mysqlconnector://root:root@db/week9", echo=False)
        self.Base = Base
        self.Base.metadata.drop_all(self.engine)
        self.create_data()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def create_data(self):
        self.Base.metadata.create_all(self.engine)
        target_path = os.path.join(os.path.dirname(__file__), '../../files/Groceries_dataset.csv')
        df = pd.read_csv(target_path)
        df.to_sql('groceries', schema='week9', con=self.engine, if_exists='append', index = False)
    
    def all_groceries(self):
        groceries = [grocerie.to_json() for grocerie in self.session.query(Groceries).all()]
        
        return groceries
    
    def all_items_from_member(self, member_no):
        items = [item.to_json() for item in self.session.query(Groceries).filter(Groceries.Member_number == member_no).all()]
        return items
