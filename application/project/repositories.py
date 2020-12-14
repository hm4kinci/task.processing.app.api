from common.managers import ProjectDatabaseManager


class ProjectRepository:
    def __init__(self):
        self._data_manager = ProjectDatabaseManager()
        super().__init__()

    def get_all(self):
        return list(self._data_manager.find())

