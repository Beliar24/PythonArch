from api.dto.response_dto.user_get_response_builder import GetUserResponseBuilder
from api.dto.response_dto.user_response_builder import UserResponseBuilder
from api.enumiration.uri import Uri
from api.lib.my_requests import MyRequests
from api.utils.json_utils import from_json


def crate_user(data):
    request = MyRequests(data)
    response = request.post(Uri.create_user.value).text

    return from_json(response, UserResponseBuilder)


def get_user(name):
    request = MyRequests()
    response = request.get(f"{Uri.get_user.value}{name}").text

    return from_json(response, GetUserResponseBuilder)
