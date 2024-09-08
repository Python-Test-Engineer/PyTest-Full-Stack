"""API Context """

from playwright.sync_api import *


def test_0171_users_api(playwright: Playwright):
    """
    Function to test the users API.

    Parameters:
    - playwright: A Playwright object representing the playwright instance.

    Returns:
    None
    """
    api_context = playwright.request.new_context(base_url="https://dummyjson.com")

    response = api_context.get("/users/1")

    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"
