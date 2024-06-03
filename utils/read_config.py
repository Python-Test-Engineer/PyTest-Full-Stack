"""Reads ini files in config folder"""

import configparser
from pathlib import Path

CG_FILE_DIR = "config"
CG_FILE = "config.ini"

# cg_fileFlaskApp = "qa.ini"

config = configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
print(f"BASE_DIR: {BASE_DIR}")
CONFIG_FILE = BASE_DIR.joinpath(CG_FILE_DIR).joinpath(CG_FILE)

config.read(CONFIG_FILE)


def get_pet_api_url():
    """GET"""
    return config["pet"]["url"]


def get_version():
    return config["framework"]["version"]


print(f"PET API: {get_pet_api_url()}")
print(f"VERSION: {get_version()}")
