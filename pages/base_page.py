from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def visit(self, url: str):
        return self._page.goto(url, wait_until="load")

    @property
    def context(self):
        return self._page.context

    def is_cookies_present(self):
        return self._page.locator("#cookie-law-info-bar").is_visible()

    def wait_for_page_load(self):
        self._page.wait_for_load_state(state="networkidle")

    def accept_all_cookies(self):
        if self.is_cookies_present():
            self._page.locator("#wt-cli-accept-all-btn").click()

    def is_page_opened(self, url: str = None):
        return url in self._page.url
