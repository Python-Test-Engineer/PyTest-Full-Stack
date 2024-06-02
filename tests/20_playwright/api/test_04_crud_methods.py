"""CRUD methods"""

import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    """
    Create an API context using Playwright.

    Args:
        playwright (Playwright): The Playwright instance.

    Returns:
        APIRequestContext: The APIRequestContext object.

    Raises:
        None.

    Examples:
        >>> api_context = api_context(playwright)
    """
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={"Content-Type": "application/json"},
    )
    yield api_context
    api_context.dispose()


def test_0175_create_user(api_context: APIRequestContext):
    """
    Creates a new user by sending a POST request to the "users/add" endpoint of the API.

    Args:
        api_context (APIRequestContext): An instance of the APIRequestContext class.

    Returns:
        None
    """
    response = api_context.post(
        "users/add", data={"firstName": "Damien", "lastName": "Smith", "age": 27}
    )
    user_data = response.json()

    assert user_data["id"] == 209
    assert user_data["firstName"] == "Damien"


def test_0176_update_user(api_context: APIRequestContext):
    # print(
    #   "Default Last Name:",
    #   api_context.get("users/1").json()["lastName"]
    # )

    response = api_context.put(
        "users/1",
        data={
            "lastName": "Smith",
            "age": 20,
        },
    )
    user_data = response.json()

    assert user_data["lastName"] == "Smith"
    assert user_data["age"] == 20


def test_0177_remove_user(api_context: APIRequestContext):
    response = api_context.delete("users/1")

    user_data = response.json()

    assert user_data["isDeleted"]
