import allure
from api.lib.base_request import BaseRequest


class MyRequests(BaseRequest):

    def __init__(self, data=None, headers=None, cookies=None):
        super().__init__(data, headers, cookies)

    def post(self, url: str):
        with allure.step(f"POST request to URL {url}"):
            return self.send(url, "POST")

    def get(self, url: str):
        with allure.step(f"GET request to URL {url}"):
            return self.send(url, "GET")

    def put(self, url: str):
        with allure.step(f"PUT request to URL {url}"):
            return self.send(url, "PUT")

    def delete(self, url: str):
        with allure.step(f"DELETE request to URL {url}"):
            return self.send(url, "DELETE")
