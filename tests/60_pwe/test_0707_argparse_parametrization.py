# https://pytest-with-eric.com/pytest-advanced/pytest-argparse-typer/

from src.pwe_argparse_yaml_reader import main
import pytest
import shlex

test_cases = [
    (
        "--configpath='config/config_pwe.yml'",  # Valid path without optional args
        "{'url': 'https://example.com/', 'port': 3001}",
    ),
    (
        "--configpath 'config/config_pwe.yml' --env='dev'",  # Valid path with optional args
        "{'url': 'https://dev.com/', 'port': 3010}",
    ),
    (
        "--env='prod' --configpath 'config/config_pwe.yml'",  # Different order
        "{'url': 'https://prod.com/', 'port': 2007}",
    ),
    (
        "--configpath 'src/config.yml' --env='dev'",  # Path doesn't exist
        "`configpath` must be a valid file path. Provided path: `src/config.yml` does not exist.",
    ),
    (
        "--configpath ''",  # Null or None value passed
        "No path provided",
    ),
    (
        "--configpath 'src/yaml_configs==config.yml'",  # Invalid path
        "`configpath` must be a valid file path. Provided path: `src/yaml_configs==config.yml` does not exist.",
    ),
    (
        "--configpath 'path/to/nonexistent/file.yml'",  # Nonexistent file
        "`configpath` must be a valid file path. Provided path: `path/to/nonexistent/file.yml` does not exist.",
    ),
]


@pytest.mark.parametrize("command, expected_output", test_cases)
def test_argparse_yaml_reader(capsys, command, expected_output):
    main(shlex.split(command))
    captured = capsys.readouterr()
    output = captured.out + captured.err
    assert expected_output in output


# Test cases
test_cases_sys_exit = [
    (
        "",  # No argument passed
        "the following arguments are required: --configpath",
    ),
    (
        "-configpath 'config/config_pwe.yml' --env 'dev'",  # Wrong flag passed
        "the following arguments are required: --configpath",
    ),
    (
        "configpath 'config/config_pwe.yml' --env 'dev'",  # No flag passed
        "the following arguments are required: --configpath",
    ),
    (
        "-+configpath 'config/config_pwe.yml' --env 'dev'",  # Wrong Type of flag passed
        "the following arguments are required: --configpath",
    ),
    (
        "--wrong_argument 'config/config_pwe.yml' --env 'dev'",  # Wrong argument name
        "the following arguments are required: --configpath",
    ),
]


@pytest.mark.parametrize("command, expected_output", test_cases_sys_exit)
def test_argparse_yaml_reader_sys_exit(capsys, command, expected_output):
    with pytest.raises(SystemExit):  # Expecting SystemExit due to argparse error
        main(shlex.split(command))
    captured = capsys.readouterr()  # Capture both stdout and stderr
    output = captured.out + captured.err  # Combine stdout and stderr
    assert expected_output in output
