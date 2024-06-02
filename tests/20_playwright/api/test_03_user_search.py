"""User Search API"""

import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    """
    Fixture function that returns an APIRequestContext object.

    :param playwright: The playwright object used to create the context.
    :type playwright: Playwright

    :return: The APIRequestContext object.
    :rtype: APIRequestContext
    """
    api_context = playwright.request.new_context(base_url="https://dummyjson.com")
    yield api_context
    api_context.dispose()


#  https://dummyjson.com/users/search?q=John


def test_0172_users_search(api_context: APIRequestContext):
    query = "Emily"
    response = api_context.get(f"/users/search?q={query}")

    users_data = response.json()

    # print("Users found:", users_data["total"])

    for user in users_data["users"]:
        # print("Checking user:", user["firstName"])
        assert query in user["firstName"]
