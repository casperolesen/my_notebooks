from flask import Flask, jsonify, request
app = Flask(__name__)

from ..my_modules.Week_8.BookDB import BookDB
from ..my_modules.Week_8.TestDB import TestDB

import sys
import os

#bookDB = BookDB()
testDB = TestDB()

@app.route('/')
def hello_world():
    path = sys.path
    #return 'Caspers Book API'
    return jsonify(path)

@app.route('/test', methods=['GET'])
def test_all_books():
    books = TestDB.all_books()
    return jsonify(books)

@app.route('/create-database', methods=['GET'])
def create_database():
    bookDB.createDatabase()
    return 'Database created..'

@app.route('/books', methods=['GET'])
def all_books():
    books = bookDB.all_books()
    return jsonify(books)

@app.route('/books/top10', methods=['GET'])
def best_books():
    books = bookDB.best_books()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def new_book():
    book_to_add = {
        'Rating': request.json.get("rating", 0),
        'Reviews': request.json.get("reviews", ""),
        'Book_title': request.json["title"],
        'Description': request.json.get('description', ""),
        'Number_Of_Pages': request.json.get("pages", 0),
        'Type': request.json.get("type", ""),
        'Price': request.json.get("price", 0)
    }
    book = bookDB.create_book(book_to_add)
    return jsonify(book)

@app.route('/books', methods=['DELETE'])
def delete_book():
    title = request.json["title"]
    status = bookDB.delete_book(title)
    return jsonify(status)

@app.route('/books', methods=['PUT'])
def edit_book():
    book_to_edit = {
        'Rating': request.json.get("rating", 0),
        'Reviews': request.json.get("reviews", ""),
        'Book_title': request.json["title"],
        'Description': request.json.get('description', ""),
        'Number_Of_Pages': request.json.get("pages", 0),
        'Type': request.json.get("type", ""),
        'Price': request.json.get("price", 0)
    }
    book = bookDB.create_book(book_to_add)
    return jsonify(book)

@app.route('/datagenerator/api/person/<int:no>', methods=['GET'])
def get_persons(no):
    persons = []

    for i in range(1, no+1):
        persons.append(i)
        persons.append({"id":i,"name":"Person "+str(i)})

    return jsonify(persons)
    #return jsonify({'tasks': tasks})