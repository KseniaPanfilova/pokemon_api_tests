import requests
from utils.logger import log_response


class HttpClient:
    def __init__(self, base_url: str, timeout=10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout

    def get(self, *, endpoint: str, headers: dict = None, params: dict = None) -> requests.Response:
        response = requests.get(url=f'{self.base_url}/{endpoint.lstrip('/')}',
                                headers=headers,
                                params=params,
                                timeout=self.timeout)
        log_response(response)
        return response

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
