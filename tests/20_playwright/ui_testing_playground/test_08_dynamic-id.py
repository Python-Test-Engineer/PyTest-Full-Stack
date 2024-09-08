from playwright.sync_api import Page, expect


def test_0201_dynamic_id(page: Page):
    """
    Navigate to a webpage with a dynamic ID and click on a button with a dynamic ID.

    Args:
        page (Page): The Page object used to interact with the webpage.

    Returns:
        None
    """
    page.goto("http://uitestingplayground.com/dynamicid")

    button = page.get_by_role("button", name="Button with Dynamic ID")
    expect(button).to_be_visible()

    button.click()
