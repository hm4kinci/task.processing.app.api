from .base import BaseDatabaseManager


class MemberDatabaseManager(BaseDatabaseManager):
    """
            Database manager to access members collection
    """
    def __init__(self):
        super().__init__()
        self._collection = self._connection.get_database().members

