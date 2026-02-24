import json
from configs.settings import TEST_DATA_FILE
from pathlib import Path


def json_to_dict(path_to_json_file: str | Path) -> dict:
    try:
        with open(path_to_json_file, encoding="utf-8") as json_file:
            result_dict = json.load(json_file)
    except FileNotFoundError:
        raise Exception(f"File not fount at{path_to_json_file}")
    return result_dict


def get_test_data(key: str) -> str:
    test_data_dict = json_to_dict(TEST_DATA_FILE)
    test_data = test_data_dict.get(key)
    return test_data
