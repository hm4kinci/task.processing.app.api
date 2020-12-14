from common.http.utils import get_data


class ClassifierBase:
    def __init__(self) -> None:
        pass

    def get_data(self, response):
        return get_data(response=response)
