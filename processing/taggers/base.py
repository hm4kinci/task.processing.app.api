from common.http.utils import get_data


class TaggerBase:
    def __init__(self, tag_class, linker=None) -> None:
        self.tag_class = tag_class
        self.linker = linker
        super().__init__()

    def get_data(self, response):
        return get_data(response=response)

    def process(self, response, threshold=0.2):
        """
            Base method for tagging. Child classes can use if they follow text,labels structure

        """
        data = self.get_data(response)

        project_entities = list()
        for entity in data:
            entity_labels = entity.get('labels')
            if entity_labels and entity_labels.get(self.tag_class, 0) > threshold:
                project_entity = dict()
                project_entity['label'] = entity['text']
                project_entity['confidence'] = entity_labels.get(self.tag_class, 0)
                project_entity = self.process_entity(project_entity)
                project_entities.append(project_entity)

        project_entities.sort(key=lambda x: x['confidence'], reverse=True)

        return project_entities

    def process_entity(self, entity):
        return entity