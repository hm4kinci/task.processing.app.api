from common.database import MongoDBConnection
from flask import session


class BaseDatabaseManager:

    def __init__(self):
        self._connection = MongoDBConnection()

    def find(self, query={}):
        """
            extends query with organization_id from session object
            put .find(query) to MongoDB
        """
        organization_id = session['organization_id']
        query.update({'organization_id': organization_id})
        return self._collection.find(query)

