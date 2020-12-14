from .base import TaggerBase


class ProjectTagger(TaggerBase):
    """
                Process project tags returned by Tagger Service
                uses base.process() to process list
    """
    def __init__(self, tag_class='MISC'):
        super().__init__(tag_class=tag_class)
