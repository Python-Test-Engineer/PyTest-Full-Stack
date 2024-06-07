# https://pytest-with-eric.com/pytest-advanced/pytest-argparse-typer/

import os
import yaml
from typing import Dict
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def parse_args(args=None) -> ArgumentParser.parse_args:
    """
    Function to parse command line arguments

    Args:
    args: list of strings to parse

    Returns:
    parsed_args: parsed arguments
    """
    argument_parser = ArgumentParser(
        description="Command line arguments for reading a configuration file",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    argument_parser.add_argument(
        "--configpath", type=str, help="Configuration file path", required=True
    )
    argument_parser.add_argument(
        "--env", type=str, default="rest", help="Select environment"
    )
    return argument_parser.parse_args(args)


def yaml_reader(path: str, env: str) -> Dict:
    """
    Function to read YAML config file

    Args:
    path: path to the YAML file

    Returns:
    data: dictionary of data from the YAML file
    """
    try:
        with open(path, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            return data[env]
    except Exception as e:
        print(f"Error reading YAML file: {e}")


def main(args=None) -> None:
    """
    Main function to read YAML file
    """
    args = parse_args(args)
    configpath = args.configpath
    env = args.env

    if len(configpath) == 0:
        print("No path provided")
    else:
        if configpath and os.path.isfile(configpath):
            print(yaml_reader(path=configpath, env=env))
        else:
            print(
                f"`configpath` must be a valid file path. Provided path: `{configpath}` does not exist."
            )


if __name__ == "__main__":
    main()
