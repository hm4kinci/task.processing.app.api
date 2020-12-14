from settings import SERVICE_URL_CONTACT_TYPE_CLASSIFICATION
from .base import ServiceBase


class ContactTypeClassifierService(ServiceBase):
    """
             Service Communication wrapper class for Classification API
    """
    def __init__(self, service_url=SERVICE_URL_CONTACT_TYPE_CLASSIFICATION):
        super().__init__(service_url=service_url)
