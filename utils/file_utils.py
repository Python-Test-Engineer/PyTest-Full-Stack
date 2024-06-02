"""File utilities"""
import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIR = BASE_DIR.joinpath("TestData")


def get_json_from_file(filename: str) -> str:
    """Get JSON from file"""
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, "r", encoding="UTF-8") as file:
        return json.load(file)


# function to read data from CSV file
def get_csv_as_dict(filename: str):
    """Get CSV as dict"""
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, "r", encoding="UTF-8") as file:
        csv_file = csv.DictReader(file)
        dict_list = list(csv_file)
    return dict_list


# get data from CSV as list
def get_data_as_list(filename: str) -> list[list[str]]:
    """Get data as list"""
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, "r", encoding="UTF-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        lines = list(reader)
    return lines


print("~~~~~~~~~~~~~")
print(get_csv_as_dict("registerApiData.csv"))

print(get_data_as_list("registerApiDataWithStatus.csv"))

## WE can create a dict with list of zipped keys and values
keys = ["a", "b", "c", "d"]
values = ["alpha", "beta", "delta"]
d = dict(zip(keys, values))
print(d)
