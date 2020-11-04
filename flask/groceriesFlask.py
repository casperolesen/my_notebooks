from flask import Flask, jsonify, request
app = Flask(__name__)

from ..my_modules.Week_9.GroceriesDB import GroceriesDB

import sys
import os

"""
winpty docker exec -it -e FLASK_APP="my_notebooks/flask/groceriesFlask.py" notebookserver bash
flask run --host=0.0.0.0
"""

groceriesDB = GroceriesDB()

@app.route('/')
def hello_world():
    return 'Caspers Groceries API'

@app.route('/api/user/items/<int:member>', methods=['GET'])
def all_items_from_member(member):
    items = groceriesDB.all_items_from_member(member)
    return jsonify(items)