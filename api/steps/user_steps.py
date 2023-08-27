from api.dto.response_dto.user_get_response_builder import GetUserResponseBuilder
from api.dto.response_dto.user_response_builder import UserResponseBuilder
from api.enumiration.uri import Uri
from api.lib.my_requests import MyRequests
from api.utils.json_utils import Utils


class UserSteps:
    @staticmethod
    def crate_user(data):
        response = MyRequests.post(Uri.create_user.value, dict(data)).text

        return Utils.from_json(response, UserResponseBuilder)

    @staticmethod
    def get_user(name):
        response = MyRequests.get(f"{Uri.get_user.value}{name}").text

        return Utils.from_json(response, GetUserResponseBuilder)
