def _is_successful(response) -> bool:
    if response is not None and response.get('success'):
        return True
    return False


def get_data(response):
    if _is_successful(response):
        return response.get('data')
    else:
        return None
