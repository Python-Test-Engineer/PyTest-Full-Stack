""" DOC """
from playwright.sync_api import Page


class MainPage:
    """DOC"""

    HEADER: str = "h1"
    MORE_INFO_LINK: str = "text=More information"

    def __init__(self, page: Page):
        self.page = page

    def verify_header_text(self):
        """DOC"""
        assert self.page.inner_text(self.HEADER) == "Example Domain"

    def select_more_information_link(self):
        """DOC"""
        with self.page.expect_navigation():
            self.page.click(self.MORE_INFO_LINK)
