from api.dto.response_dto.user_get_response_builder import GetUserResponseBuilder
from api.dto.response_dto.user_response_builder import UserResponseBuilder
from api.lib.config_parser import get_users_config
from api.lib.my_requests import MyRequests
from api.utils.json_utils import from_json


def crate_user(data):
    request = MyRequests(data)
    response = request.post(get_users_config("user", "create_user")).text

    return from_json(response, UserResponseBuilder)


def get_user(name):
    request = MyRequests()
    get_user_endpoint = get_users_config("user", "get_user")
    response = request.get(f"{get_user_endpoint}{name}").text

    return from_json(response, GetUserResponseBuilder)
