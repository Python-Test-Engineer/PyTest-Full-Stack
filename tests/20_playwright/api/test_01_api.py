"""Basic API """

from playwright.sync_api import *


def test_0170_users_api(page: Page):
    """
    Test the users API by making a request to the specified URL and asserting the presence of certain data.

    Parameters:
    - page (Page): The Page object used to make the API request.

    Returns:
    None
    """
    response = page.goto("https://dummyjson.com/users/1")

    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"
