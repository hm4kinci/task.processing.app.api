from common.managers import MemberDatabaseManager


class MemberRepository:
    def __init__(self):
        self._data_manager = MemberDatabaseManager()
        super().__init__()

    def get_all(self):
        return list(self._data_manager.find())

