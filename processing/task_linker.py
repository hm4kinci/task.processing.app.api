from processing.linkers import (ProjectLinker, MemberLinker)
from processing.results import (TaskProcessingResult, TaskLinkingResult)


class TaskLinker:
    def __init__(self) -> None:
        self._repositories = dict()
        pass

    def register_repository(self, key, repository):
        self._repositories[key] = repository

    def process(self, task_processing_result: TaskProcessingResult):
        """
            Linking logic implemented here

        """
        task_linking_results = TaskLinkingResult()
        project_repository = self._repositories['project']
        task_linking_results.projects = ProjectLinker.create(project_repository).process(task_processing_result.projects)

        member_repository = self._repositories['member']
        task_linking_results.contact_persons = MemberLinker.create(member_repository).process(task_processing_result.contact_persons)
        return task_linking_results

