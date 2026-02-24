from playwright.sync_api import Page, Locator

class CareerCardComponent:
    def __init__(self, page: Page, locator: Locator | str):
        self._page = page
        self._locator = locator if isinstance(locator, Locator) else self._page.locator(locator)
        self._position_title = self._locator.locator(".position-title")
        self._position_department = self._locator.locator(".position-department")
        self._position_location = self._locator.locator(".position-location")
        self._view_role_link = self._locator.get_by_role("link", name="View Role")

    def get_position_title(self):
        return self._position_title.inner_text()

    def get_position_department(self):
        return self._position_department.inner_text()

    def get_position_location(self):
        return self._position_location.inner_text()

    def click_view_role_link(self):
        self._view_role_link.click()

