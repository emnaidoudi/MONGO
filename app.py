from flask import Flask, Response,jsonify
from flask_pymongo import PyMongo,MongoClient
import os
from bson.json_util import dumps
import json

app = Flask(__name__)
#-------------------------------------------------------------------------------------
def save_to_intents(data):
    data={"intents":data}
    with open('intents.json', 'w') as outfile:
        json.dump(data, outfile)
#-------------------------------------------------------------------------------------
client = MongoClient(
    "mongodb://localhost:27017/")
db = client.mydb

@app.route("/cities")
def home_page():
    cities = db.cities.find()
    #list(cities)[0]
    return dumps(cities)


@app.route("/intents")
def get_user_intents():
    intents = db.intents.find()
    save_to_intents(dumps(intents))
    intents=db.intents.find()
    return Response(dumps(intents)  ,mimetype='application/json')


  

#render_template("index.html",
#online_users=online_users)

if __name__ == '__main__':
    app.run(debug=True)
