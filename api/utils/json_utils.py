import json


class Utils:

    @staticmethod
    def from_json(json_str, class_type):
        json_dict = json.loads(json_str)
        if isinstance(json_dict, dict):
            return class_type(**json_dict)
        return None
