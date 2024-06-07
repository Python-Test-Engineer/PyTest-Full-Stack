import pytest
import shlex
from src.pwe_argparse_yaml_reader import main, yaml_reader
from typer.testing import CliRunner
from src.pwe_typer_yaml_reader import app


# Fixture to get user command-line arguments
@pytest.fixture
def get_user_input(request):
    configpath = str(request.config.getoption("--configpath"))
    env = str(request.config.getoption("--env"))
    return configpath, env


# Testing argparse_yaml_reader()
def test_argparse_yaml_reader(capsys, get_user_input):
    configpath, env = get_user_input
    expected_output = str(yaml_reader(configpath, env))
    main(shlex.split("--configpath " + configpath + " --env " + env))
    output = capsys.readouterr().out.rstrip()
    assert expected_output in output


# Testing typer_yaml_reader()
def test_typer_yaml_reader(get_user_input):
    configpath, env = get_user_input
    expected_output = str(yaml_reader(configpath, env))
    runner = CliRunner()
    result = runner.invoke(app, shlex.split(configpath + " --env " + env))
    assert expected_output in result.stdout
