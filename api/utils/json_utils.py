import json


def from_json(json_str, class_type):
    json_dict = json.loads(json_str)

    if isinstance(json_dict, dict):
        return class_type(**json_dict)

    if isinstance(json_dict, list):
        return class_type(*json_dict)

