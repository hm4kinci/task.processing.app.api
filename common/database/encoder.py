import json
import datetime
from bson import ObjectId
from uuid import UUID


class BSONtoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, ObjectId) or isinstance(obj, UUID):
            return str(obj)
        return json.JSONEncoder.default(self, obj)