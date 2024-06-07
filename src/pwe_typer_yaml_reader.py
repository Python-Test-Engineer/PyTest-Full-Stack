# https://pytest-with-eric.com/pytest-advanced/pytest-argparse-typer/

import yaml
import typer
import os

app = typer.Typer()


@app.command()
def main(configpath: str, env: str = "rest") -> None:
    """
    Main function to read YAML file

    Args:
    configpath: path to the YAML file

    Returns:
    None
    """
    if configpath and os.path.isfile(configpath):
        print(yaml_reader(configpath, env))
    else:
        print(
            f"`configpath` must be a valid file path. Provided path: `{configpath}` does not exist."
        )


def yaml_reader(path: str, env: str) -> None:
    """
    Function to read YAML config file
    """
    try:
        with open(path, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            return data[env]
    except Exception as e:
        print(f"Error reading YAML file: {e}")


if __name__ == "__main__":
    app()
