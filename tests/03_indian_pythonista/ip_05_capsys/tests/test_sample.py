"""docstring"""

import json
import os

from .sample import save_dict


def test_1105_save_dict(tmpdir, capsys):
    """docstring"""
    filepath = os.path.join(tmpdir, "test.json")
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, "r", encoding="utf-8")) == _dict
    assert capsys.readouterr().out == "saved\n"
