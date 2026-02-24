from pages.base_page import BasePage
from playwright.sync_api import Page


class CareersPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._see_all_qa_jobs_button = page.get_by_role("link", name="See all QA jobs")

    def click_see_all_qa_jobs_button(self):
        self._see_all_qa_jobs_button.click()