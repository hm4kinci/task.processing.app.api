from .base import TaggerBase


class ContactPersonTagger(TaggerBase):
    """
        Process contact person tags returned by Tagger Service
        uses base.process()

    """
    def __init__(self, tag_class='PERSON', linker=None):
        super().__init__(tag_class=tag_class, linker=linker)
