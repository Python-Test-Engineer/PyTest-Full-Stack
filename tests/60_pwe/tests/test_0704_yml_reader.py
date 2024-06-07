from src.pwe_argparse_yaml_reader import main
from typer.testing import CliRunner
from src.pwe_typer_yaml_reader import app


def test_argparse_yaml_with_list(capsys):
    test_args = ["--configpath", "config/config_pwe.yml", "--env", "rest"]
    expected_output = "{'url': 'https://example.com/', 'port': 3001}"
    main(test_args)
    output = capsys.readouterr().out.rstrip()
    assert expected_output in output
