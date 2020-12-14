import pytest
from processing.classifiers import ContactTypeClassifier
from processing.services import ContactTypeClassifierService


@pytest.mark.integration
def test_contact_type_classifier():
    text = 'I emailed John yesterday'
    contact_type_service_response = ContactTypeClassifierService().call(text)
    contact_type = ContactTypeClassifier().process(contact_type_service_response, threshold=0.2)

    if contact_type is not None:
        assert contact_type.get('value') is not None
        assert contact_type.get('confidence') is not None
        assert contact_type.get('confidence') >= 0
        assert contact_type.get('confidence') <= 1

