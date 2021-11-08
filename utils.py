import json


def read_json(json_path: str):
    """Reads a json file.

    :param json_path: path to json file.
    :return: json content
    """
    with open(json_path) as f:
        return json.load(f)
