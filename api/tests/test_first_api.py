import pytest
import allure
from api.dto.request_dto.user import User
from api.lib.assertions import assert_json_value_be_name, assert_json_has_not_key
from api.steps.user_steps import get_user, crate_user

names = ["user", "user1"]


@allure.description("create user")
@pytest.mark.parametrize('name', names)
def test_create_user(name):
    data = User(0, name, 'sfgsd', 'ertf', 'tewe', 'sdgdfgd', '24646252', 0).to_dict()

    response = crate_user(data)

    assert_json_value_be_name(response.code, 200, "Wrong response code")
    assert_json_value_be_name(response.type, "unknown", "The response doesn't have username param")


@pytest.mark.parametrize('name', names)
@allure.description("This test return dict of users")
def test_get_user(name):
    response = get_user(name)

    assert_json_value_be_name(response.username, name, "The response doesn't have username param")
    assert_json_has_not_key(response.username, "username1")
