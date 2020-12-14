import pytest
from processing.services import TaggerService
from processing.taggers import (ProjectTagger, ContactPersonTagger, DateTagger)


@pytest.mark.integration
def test_project_tagger():
    text = 'I emailed John yesterday about Project Alpha'
    tagger_service_response = TaggerService().call(text)
    projects = ProjectTagger().process(tagger_service_response)

    assert projects is not None
    assert isinstance(projects, list)
    for project in projects:
        label = project.get('label')
        assert label is not None

        confidence = project.get('confidence')
        assert confidence is not None
        assert confidence <= 1
        assert confidence >= 0


@pytest.mark.integration
def test_contact_person_tagger():
    text = 'I emailed John yesterday about Project Alpha'
    tagger_service_response = TaggerService().call(text)
    contact_persons = ContactPersonTagger().process(tagger_service_response)

    assert contact_persons is not None
    assert isinstance(contact_persons, list)
    for project in contact_persons:
        label = project.get('label')
        assert label is not None

        confidence = project.get('confidence')
        assert confidence is not None
        assert confidence <= 1
        assert confidence >= 0


@pytest.mark.integration
def test_date_tagger():
    text = '21 January 2020: I emailed John yesterday about Project Alpha'
    tagger_service_response = TaggerService().call(text)
    dates = DateTagger().process(tagger_service_response)

    assert dates is not None
    assert isinstance(dates, list)
    for project in dates:
        label = project.get('label')
        assert label is not None

        confidence = project.get('confidence')
        assert confidence is not None
        assert confidence <= 1
        assert confidence >= 0

        #todo implement parsed date check
