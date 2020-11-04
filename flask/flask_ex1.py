from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! FROM MY_NOTEBOOKS!!!'

@app.route('/datagenerator/api/person/<int:no>', methods=['GET'])
def get_persons(no):
    persons = []

    for i in range(1, no+1):
        persons.append(i)
        persons.append({"id":i,"name":"Person "+str(i)})

    return jsonify(persons)
    #return jsonify({'tasks': tasks})
