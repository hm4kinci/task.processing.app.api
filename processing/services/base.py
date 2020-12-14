import requests
from common.http.async_http import run as async_http


class ServiceBase:
    def __init__(self, service_url=None):
        self._service_url = service_url

    def parallel_call(self, queries):
        """
            makes async parallel call to the service
            requires queries: list ,  ['query'] in items
        """
        return async_http(self._service_url, queries, ['query'])

    def call(self, query):
        """
            makes sync call to the service
        """
        payload = {'query': query}
        response = requests.get(self._service_url, params=payload)
        return response.json()

