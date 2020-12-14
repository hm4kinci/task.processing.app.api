from pymongo import MongoClient
from settings import  (MONGO_DB_CONNECTION_URI, MONGO_DB_DEFAULT)


class MongoDBConnection:
    def __init__(self) -> None:
        self._connection = MongoClient(MONGO_DB_CONNECTION_URI)
        self._database = MONGO_DB_DEFAULT

    def get_database(self):
        return self._connection[self._database]
