"""docstring"""
import json


def save_dict(_dict, filepath) -> None:
    """docstring"""
    json.dump(_dict, open(filepath, "w", encoding="utf-8"))
    print("saved")
