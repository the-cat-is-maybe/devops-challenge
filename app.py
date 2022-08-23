from os import environ

from bson import json_util
from bson.objectid import ObjectId
from flask import Flask, jsonify
from flask_pymongo import PyMongo

from src.mongoflask  import MongoJSONEncoder, ObjectIdConverter, find_restaurants_2

app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI")
app.json_encoder = MongoJSONEncoder
app.url_map.converters["objectid"] = ObjectIdConverter
mongo = PyMongo(app)


@app.route("/api/v1/restaurant")
def restaurants():
    restaurants = find_restaurants_2(mongo)
    return jsonify(restaurants)

@app.route("/api/v1/restaurant/<id>")
def restaurant(id):
    restaurants = find_restaurants_2(mongo, "_id", ObjectId(id))
    if restaurants == {}:
        return '', 204
    else:
        return jsonify(restaurants)

@app.route("/api/v2/restaurant/<field>/<search>")
def restaurant_wide_search(field,search):
    restaurants = find_restaurants_2(mongo, field, search)
    if restaurants == {}:
        return '', 204
    else:
        return jsonify(restaurants)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8080)
