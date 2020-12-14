from .base import LinkerBase


class ProjectLinker(LinkerBase):
    """
             Entity Linker class for Project
             Links tags with entities within given user context/repository
             Should be created with a factory method create()
    """
    _repository = None

    def __init__(self) -> None:
        """
             WARNING: Should be created with a factory method create()
        """
        super().__init__()

    def process(self, project_tags):
        """
                Link tags with entities
        """
        assert self._repository is not None

        projects = list()
        lookup_list = ProjectLinker.create_keys(self._repository.get_all())
        for project_tag in project_tags:
            text = project_tag.get('label').lower()
            for lookup_item in lookup_list:
                if text in lookup_item['keys']:
                    project_tag['linked_entity'] = {'id': lookup_item['_id'], 'name': lookup_item['name'], 'code': lookup_item['code']}
            projects.append(project_tag)
        return projects

    @staticmethod
    def create(repository):
        """
                Creates a linker object with given member repository
        """
        linker = ProjectLinker()
        linker._repository = repository
        return linker

    @staticmethod
    def create_keys(projects):
        """
                Helper method to create search keys based on entity
        """
        for project in projects:
            keys = [name_variation.lower() for name_variation in project.get('name_variations', [])]
            keys.append(project['name'].lower())
            project['keys'] = keys
        return projects
