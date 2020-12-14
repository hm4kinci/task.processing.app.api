from .base import BaseDatabaseManager


class ProjectDatabaseManager(BaseDatabaseManager):
    """
         Database manager to access projects collection
    """
    def __init__(self):
        super().__init__()
        self._collection = self._connection.get_database().projects

