from datetime import date, datetime

import isodate as iso
from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter
import re
import urllib.parse


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)

##!## This next block is deprecated and should be considered for removal.
## def find_restaurants(mongo, _id=None):
##    query = {}
##    if _id:
##        query["_id"] = ObjectId(_id)
##    result = mongo.db.restaurant.find(query)
##    result_count = len(list(result.clone()))
##    if result_count > 1:
##        return list(result)
##    else:
##        return next(result, {})

def find_restaurants_2(mongo, field=None, search=None):
    query = {}
    if field:
        if type(search) == str:
            search = urllib.parse.unquote(search)
            search = re.compile(search+'.*', re.IGNORECASE)
        query[urllib.parse.unquote(field)] = search 
    print (query)
    result = mongo.db.restaurant.find(query)
    result_count = len(list(result.clone()))
    if result_count > 1:
        return list(result)
    else:
        return next(result, {})