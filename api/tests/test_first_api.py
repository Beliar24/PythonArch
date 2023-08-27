import pytest
from api.dto.request_dto.user import User
from api.lib.assertions import Assertions
from api.lib.base_case import BaseCase
import allure

from api.steps.user_steps import UserSteps


@allure.epic("Create and get users")
class TestFirstApi(BaseCase):
    names = ["user", "user1"]

    @allure.description("create user")
    @pytest.mark.parametrize('name', names)
    def test_create_user(self, name):
        data = User.get_dto_dict(0, name, 'sfgsd', 'ertf', 'tewe', 'sdgdfgd', '24646252', 0)

        response = UserSteps.crate_user(data)

        Assertions.assert_json_value_be_name(response.code, 200, "Wrong response code")
        Assertions.assert_json_value_be_name(response.type, "unknown", "The response doesn't have username param")

    @pytest.mark.parametrize('name', names)
    @allure.description("This test return dict of users")
    def test_get_user(self, name):
        response = UserSteps.get_user(name)

        Assertions.assert_json_value_be_name(response.username, name, "The response doesn't have username param")
        Assertions.assert_json_has_not_key(response.username, "username1")
