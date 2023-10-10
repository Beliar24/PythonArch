import requests

from api.utils.environment import ENV_OBJECT


class BaseRequest:

    def __init__(self, data=None, headers=None, cookies=None):
        self.data = data or {}
        self.headers = headers or {}
        self.cookies = cookies or {}

    def send(self, url: str, method: str):
        url = f"{ENV_OBJECT.get_base_url()}{url}"

        if method == "GET":
            response = requests.get(url, params=self.data, headers=self.headers, cookies=self.cookies)
        elif method == "POST":
            response = requests.post(url, json=self.data, headers=self.headers, cookies=self.cookies)
        elif method == "PUT":
            response = requests.put(url, json=self.data, headers=self.headers, cookies=self.cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=self.data, headers=self.headers, cookies=self.cookies)
        else:
            raise Exception(f"Bad HTTP method {method} was received")

        return response
