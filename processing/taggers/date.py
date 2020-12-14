from .base import TaggerBase
import dateparser


class DateTagger(TaggerBase):
    """
            Process date tags returned by Tagger Service
            uses base.process() to process list
            uses self.process_entity() to process list items

    """
    def __init__(self, tag_class='DATE'):
        super().__init__(tag_class=tag_class)

    def process_entity(self, entity):
        """
            Parses retrieved date-time text.
            dateparser.parse()
                returns null if not parsed
                does fuzzy matching

        """
        entity['parsed_date'] = dateparser.parse(entity.get('label'))
        return entity

