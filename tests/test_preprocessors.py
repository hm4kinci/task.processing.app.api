import pytest
from processing.preprocessors import SpellChecker


@pytest.mark.integration
def test_spell_checker():
    spell_checker = SpellChecker()
    body = 'Meetign wiht Michaol and Geprge'

    text, suggested_words = spell_checker.process(text=body)

    if text is not None:
        assert text is not None
    if len(text) == 0:
        assert len(text) == 0
    assert isinstance(text, str)
    assert suggested_words is not None
    assert isinstance(suggested_words, list)

    for suggested_word in suggested_words:
        assert suggested_word.get('misspelled_word') is not None
        assert suggested_word.get('overall_score') is not None
        assert suggested_word.get('overall_score') >= 0
        assert suggested_word.get('overall_score') <= 1
        assert suggested_word.get('suggested_word') is not None
        assert len(suggested_word.get('suggested_word')) > 0


