
from requests import Response


class Assertions:
    @staticmethod
    def assert_json_value_be_name(response: Response, expected_value, error_message):
        assert response == expected_value, f"Response JSON doesn't have value {expected_value}"
        assert response == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        assert name in response, f"Response doesn't have key {name}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        assert name not in response, f"Response have key {name}"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        for name in names:
            assert name in response, f"Response doesn't have key {name}"
