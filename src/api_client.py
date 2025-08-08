import requests


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        return requests.get(url=f'{self.base_url}/{endpoint}')
