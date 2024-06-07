import base64
import os
import pytest
import pytest_html
from pytest_metadata.plugin import metadata_key

from sqlmodel import Session
from task_manager.db import DB
from task_manager.model import Tasks, TaskStatus


@pytest.fixture
def task1():
    """
    Create a Task 1
    """
    task1 = Tasks(
        title="Go to the Gym",
        description="Visit Gym at 09:00",
        status=TaskStatus.NOT_STARTED,
    )
    yield task1


@pytest.fixture
def task2():
    """
    Create a Task 2
    """
    task2 = Tasks(
        title="Buy Groceries",
        description="Large shopping list - buy at 12:00",
        status=TaskStatus.NOT_STARTED,
    )
    yield task2


@pytest.fixture
def db_instance(scope="session"):
    """
    Create a DB Instance
    """
    db = DB()
    yield db


@pytest.fixture
def session(db_instance, scope="session"):
    """
    Create a Session, close after test session, uses `db_instance` fixture
    """
    session = Session(db_instance.engine)
    yield session
    session.close()


@pytest.fixture
def db_instance_empty(db_instance, session, scope="function"):
    """
    Create an Empty DB Instance, uses `db_instance` and `session` fixtures
    """
    # Clear DB before test function
    db_instance.delete_all_tasks(session=session)
    yield db_instance

    # Clear DB after test function
    db_instance.delete_all_tasks(session=session)


def pytest_addoption(parser):
    parser.addoption("--configpath", action="store", help="Location to YAML file")
    parser.addoption("--env", action="store", help="Environment to read from YAML file")


def pytest_html_report_title(report):
    report.title = "Pytest HTML Report Example"


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Pytest With Eric"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # Assuming your screenshot is saved correctly at the specified path
        screenshot_path = "./screenshots/pytest-html.png"
        with open(screenshot_path, "rb") as image_file:
            encoded_string = base64.b64encode(
                image_file.read()
            ).decode()  # https://github.com/pytest-dev/pytest-html/issues/265
        extra.append(pytest_html.extras.png(encoded_string))
        report.extra = extra
