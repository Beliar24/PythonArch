import json.decoder

from requests import Response


def get_cookie(response: Response, cookie_name):
    assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name}"
    return response.cookies[cookie_name]


def get_header(response: Response, header_name):
    assert header_name in response.cookies, f"Cannot find header with name {header_name}"
    return response.headers[header_name]


def get_json_values(response: Response, name):
    try:
        response_as_dict = response.json()
    except json.decoder.JSONDecodeError:
        assert False, f"Response is not JSON Format. Response text is {response.text}"
    assert name in response_as_dict, f"Response JSON doesn't key {name}"
    return response_as_dict[name]
