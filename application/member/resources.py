from common.base_data_resource import BaseDataResource
from .repositories import MemberRepository


class MemberResource(BaseDataResource):

    def __init__(self) -> None:
        self._repository = MemberRepository()
        super().__init__()

    def get(self):
        return self.success(self._repository.get_all())
