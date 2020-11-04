from app import app

import os
import json
from flask import jsonify, render_template

with open('recipes.json','r') as jsonfile:
        diction = json.load(jsonfile)

@app.route("/")
def index():
    return render_template('./index.html')

@app.route("/recipes")
def recipes():
    r = {}
    for key, recipe in diction['recipes'].items():
        r[key] = {}
        r[key]['category'] = recipe['category']
        r[key]['name'] = recipe['name']
        r[key]['preparation_time'] = recipe['preparation_time']
    return jsonify(r)

@app.route("/recipe/<id>")
def recipe(id):
    try:
        return jsonify(diction['recipes'][id])
    except: 
        e = sys.exc_info()[0]
        return jsonify({"code":400,"error":"no recipe exist with id: "+id}),400

@app.route('/<path:path>')
def catch_all(path):
    resp = {"code":400,"error":path+" is not a valid resource on this server"}
    return jsonify(resp), 400 # second value in returned tuple is the status code
