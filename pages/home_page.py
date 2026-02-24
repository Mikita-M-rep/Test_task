from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._header = page.locator("#navigation")
        self._footer = page.locator("#footer")
        self._main_sections = page.locator("main.flexible-layout")

    def is_main_sections_present(self):
        sections = self._main_sections.locator("section").all()
        for section in sections:
            section.scroll_into_view_if_needed()
            if not section.is_visible():
                return False
        return True

    def is_header_present(self):
        return self._header.is_visible()

    def is_footer_present(self):
        return self._footer.is_visible()
