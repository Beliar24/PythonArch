import pytest
from api.dto.user import User
from api.enumiration.uri import Uri
from api.lib.base_case import BaseCase
from api.lib.assertions import Assertions
from api.lib.my_requests import MyRequests
import allure


@allure.epic("Create and get users")
class TestFirstApi(BaseCase):
    names = ["user", "user1"]

    @allure.description("create user")
    @pytest.mark.parametrize('name', names)
    def test_create_user(self, name):
        data = User(0, name, 'sfgsd', 'ertf', 'tewe', 'sdgdfgd', '24646252', 0).__dict__

        response = MyRequests.post(Uri.create_user.value, dict(data))

        assert response.status_code == 200, "Wrong response code"
        Assertions.assert_json_value_be_name(response, "type", "unknown", "The response doesn't have username param")

    @pytest.mark.parametrize('name', names)
    @allure.description("This test return dict of users")
    def test_get_user(self, name):
        response = MyRequests.get(f"{Uri.get_user.value}{name}")

        assert response.status_code == 200, "Wrong response code"

        Assertions.assert_json_value_be_name(response, "username", name, "The response doesn't have username param")
        Assertions.assert_json_has_not_key(response, "username1")
