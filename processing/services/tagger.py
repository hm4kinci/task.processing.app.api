from settings import SERVICE_URL_TAGGER
from .base import ServiceBase


class TaggerService(ServiceBase):
    """
         Service Communication wrapper class for Tagger API
    """
    def __init__(self, service_url=SERVICE_URL_TAGGER):
        super().__init__(service_url=service_url)
