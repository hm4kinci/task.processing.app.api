from .base import LinkerBase


class MemberLinker(LinkerBase):
    """
         Entity Linker class for Member
         Links tags with entities within given user context/repository
         Should be created with a factory method create()
    """
    _repository = None

    def __init__(self) -> None:
        """
             WARNING: Should be created with a factory method create()
        """
        super().__init__()

    def process(self, contact_person_tags: list):
        """
             Link tags with entities
        """
        assert self._repository is not None
        members = list()
        lookup_list = MemberLinker.create_keys(self._repository.get_all())
        for contact_person_tag in contact_person_tags:
            text = contact_person_tag.get('label').lower()
            for lookup_item in lookup_list:
                if text in lookup_item['keys']:
                    contact_person_tag['linked_entity'] = {'id': lookup_item['_id'], 'name': lookup_item['name'], 'email': lookup_item['email']}
            members.append(contact_person_tag)
        return members

    @staticmethod
    def create(repository):
        """
             Creates a linker object with given member repository
        """
        linker = MemberLinker()
        linker._repository = repository
        return linker

    @staticmethod
    def create_keys(members):
        """
            Helper method to create search keys based on entity
        """
        for member in members:
            keys = [name_variation.lower() for name_variation in member.get('name_variations',[])]
            keys.append(member['name'].lower())
            member['keys'] = keys
        return members



