from processing.services import (ContactTypeClassifierService, TaggerService)
from processing.taggers import (ContactPersonTagger, ProjectTagger, DateTagger)
from processing.classifiers import (ContactTypeClassifier)
from processing.preprocessors import SpellChecker
from processing.results import  (TaskProcessingResult)


class TaskProcessor:
    def __init__(self) -> None:
        self._repositories = dict()
        pass

    def register_repository(self, key, repository):
        self._repositories[key] = repository

    def process(self, text_input) -> TaskProcessingResult:
        """
            Processing logic implemented here

        """

        task_processing_result = TaskProcessingResult()

        task_processing_result.corrected_text, suggested_words = SpellChecker().process(text_input, min_correction_score=0.80)

        contact_type_service_response = ContactTypeClassifierService().call(task_processing_result.corrected_text)
        task_processing_result.contact_type = ContactTypeClassifier().process(contact_type_service_response, threshold=0.2)

        tagger_service_response = TaggerService().call(task_processing_result.corrected_text)
        task_processing_result.projects = ProjectTagger().process(tagger_service_response)
        task_processing_result.contact_persons = ContactPersonTagger().process(tagger_service_response)
        task_processing_result.dates = DateTagger().process(tagger_service_response)

        return task_processing_result

