import re
import Levenshtein
from nltk.stem import PorterStemmer
from spellchecker import SpellChecker as spell_checker


class SpellChecker:
    """
         Context-UNAWARE spell checking following Norvig's algorithm
         can be slow for bigger edit_distance values.
         todo: consider implementing symspell
         todo: consider implementing a context-aware model (ner, mask modelling)
    """
    def __init__(self) -> None:
        self._spell_checker = spell_checker(distance=3)
        self._spell_checker.word_frequency.load_words(['skype', 'texted'])
        self._stemmer = PorterStemmer()

    def process(self, text: str,
                ignore_shorter_than=0,
                min_correction_score=0.5
                ) -> (str, list):
        """
                 processes given input and returns corrected version
            """
        if text is None or len(text) == 0:
            return text

        min_suggestion_score = 0.1
        words = self._spell_checker.split_words(text.lower())
        misspelled_words = self._spell_checker.unknown(words)
        suggested_words = []

        for misspelled_word in misspelled_words:
            if len(misspelled_word) < ignore_shorter_than:
                continue

            spelling_suggestions = self._spell_checker.candidates(misspelled_word)
            spelling_suggestions = [
                (candidate, self._spell_checker.word_probability(candidate, len(spelling_suggestions)))
                for candidate in spelling_suggestions
            ]
            spelling_suggestions.sort(key=lambda candidate: candidate[1], reverse=True)
            spelling_suggestions = spelling_suggestions[:5]
            sum_of_scores = sum(candidate[1] for candidate in spelling_suggestions)
            spelling_suggestions = [{
                'word': candidate[0],
                'overall': max(Levenshtein.ratio(candidate[0], misspelled_word), (0 if sum_of_scores == 0 else candidate[1] / sum_of_scores))
            } for candidate in spelling_suggestions]
            spelling_suggestions = [candidate for candidate in spelling_suggestions
                                    if candidate['overall'] > min_suggestion_score]
            spelling_suggestions.sort(key=lambda candidate: candidate['overall'], reverse=True)
            if len(spelling_suggestions) > 0:
                best_spelling_suggestion = spelling_suggestions[0]
                spelling_based_suggestion = dict()
                spelling_based_suggestion['misspelled_word'] = misspelled_word
                spelling_based_suggestion['overall_score'] = best_spelling_suggestion.get('overall')
                spelling_based_suggestion['suggested_word'] = best_spelling_suggestion.get('word')
                suggested_words.append(spelling_based_suggestion)

        for suggested_word in suggested_words:
            overall_score = suggested_word.get('overall_score',0.0)
            if overall_score >= min_correction_score:
                src_word = re.compile(suggested_word.get('misspelled_word'), re.IGNORECASE)
                text = src_word.sub(suggested_word.get('suggested_word'), text)

        return text, suggested_words
