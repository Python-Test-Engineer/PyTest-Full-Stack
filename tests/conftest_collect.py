import os
import sys
import random
import pytest
from datetime import datetime

# interesting note - the main source code to see how PyTest works is in the dunder folders...
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from pyboxen import boxen
from rich.console import Console

console = Console()

# ----- OUTPUT FILE AND LOCATION -----
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# practically a GUID...
FILENAME = f"./results/collect_{report_date}_{random.randint(1_000_000, 9_999_999)}.csv"


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):

    with open(f"{FILENAME}", "a") as f:
        for test in items:

            # keyword order is:
            # test name - markers - module name - folder - parent folder/grandparent folder - root folder
            # we have no markers in tests_01_collect_tests
            all_keywords = [str(x) for x in test.keywords]
            all_keywords = ("|").join(all_keywords)

            # print(f"KEYWORDS: \n{all_keywords}\n")
            # we can produce a --collect-only type of report of all test that we are going to run
            list_markers = [
                str(getattr(test.own_markers[j], "name"))
                for j in range(len(test.own_markers))
            ]
            all_markers = ("-").join(list_markers)
            test_nodeid = test.nodeid
            # bdd tests have a different format
            if "bdd" in test_nodeid:
                test_id = test.name.split("_")[2]
            else:
                test_id = test.name.split("_")[1]

            f.write(f"{test_id}|{test.name}|{all_keywords}|{all_markers}\n")
        pytest.exit("Running Collect Only finished", returncode=0)
