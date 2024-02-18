import os
from datetime import datetime

from api.utils.settings import current_location


class Logger:
    file_name = current_location("logs") + f'log_' + str(datetime.now().strftime("%Y-%m-%d")) + ".log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as file:
            file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, method: str, headers: dict, cookies: dict):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"\nREQUEST\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.now())}\n"
        data_to_add += f"Request: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request Headers: {headers}\n"
        data_to_add += f"Request Cookies: {cookies}\n"
        data_to_add += f"Request Data: {data}\n"
        data_to_add += f"\n"

        cls._write_log_to_file(data_to_add)
