from common.base_data_resource import BaseDataResource
from .repositories import ProjectRepository


class ProjectResource(BaseDataResource):
    def __init__(self) -> None:
        self._repository = ProjectRepository()
        super(ProjectResource, self).__init__()

    def get(self):
        return self.success(self._repository.get_all())

