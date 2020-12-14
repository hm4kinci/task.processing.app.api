import pytest
from processing.services import ContactTypeClassifierService
from processing.services import TaggerService


@pytest.mark.integration
def test_contact_type_classifier_service():
    text = 'I emailed John yesterday'

    contact_type_service_response = ContactTypeClassifierService().call(text)

    assert contact_type_service_response is not None
    success = contact_type_service_response.get('success')
    assert success is not None
    assert success is True

    if contact_type_service_response.get('success'):
        assert contact_type_service_response.get('data') is not None
        assert isinstance(contact_type_service_response.get('data'), list)
        for item in contact_type_service_response.get('data'):
            assert item.get('value') is not None
            assert item.get('confidence') is not None
            assert item.get('confidence') <= 1
            assert item.get('confidence') >= 0


@pytest.mark.integration
def test_contact_type_classifier_service_with_empty_input():
    text = None

    contact_type_service_response = ContactTypeClassifierService().call(text)

    assert contact_type_service_response is not None
    success = contact_type_service_response.get('success')
    assert success is not None
    assert success is not True


@pytest.mark.integration
def test_tagger_service():
    text = 'I emailed John yesterday'

    tagger_service_response = TaggerService().call(text)

    assert tagger_service_response is not None
    success = tagger_service_response.get('success')
    assert success is not None
    assert success is True

    if tagger_service_response.get('success'):
        assert tagger_service_response.get('data') is not None
        assert isinstance(tagger_service_response.get('data'), list)
        for item in tagger_service_response.get('data'):
            assert item.get('text') is not None
            assert item.get('labels') is not None
            labels = item.get('labels')
            assert isinstance(labels, dict)

            for key in labels.keys():
                assert key in ['PERSON', 'MISC', 'DATE', 'LOCATION']
                confidence = labels[key]
                assert confidence is not None
                assert confidence >= 0
                assert confidence <= 1


@pytest.mark.integration
def test_tagger_service_with_empty_input():
    text = None

    tagger_service_response = TaggerService().call(text)

    assert tagger_service_response is not None
    success = tagger_service_response.get('success')
    assert success is not None
    assert success is not True
