from components.career_card_component import CareerCardComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError


class OpenPositionsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._filter_location_dropdown = page.locator("#filter-by-location")
        self._filter_department_dropdown = page.locator("#filter-by-department")
        self._career_position_list = page.locator("#jobs-list")
        self._no_jobs_label = page.locator(".no-job-result")

    def filter_location(self, location: str):
        with self._page.expect_response("**postings/insiderone**"):
            self._filter_location_dropdown.select_option(label=location)
        try:
            expect(self._career_position_list.locator(".position-list-item")) \
                .not_to_have_count(0, timeout=20000)
        except PlaywrightTimeoutError:
            expect(self._no_jobs_label).to_be_visible()

    def filter_department(self, department):
        self._filter_department_dropdown.select_option(label=department)

    def get_career_cards(self) -> list[CareerCardComponent]:
        cards_locator = self._career_position_list.locator(".position-list-item")
        return [
            CareerCardComponent(self._page, cards_locator.nth(i))
            for i in range(cards_locator.count())
        ]

    def is_cards_title_match(self, title):
        career_cards = self.get_career_cards()
        return len(career_cards) == len([card for card in career_cards if title in card.get_position_title()])

    def is_cards_department_match(self, department):
        career_cards = self.get_career_cards()
        return len(career_cards) == len([card for card in career_cards if department in card.get_position_department()])

    def is_cards_location_match(self, location):
        career_cards = self.get_career_cards()
        return len(career_cards) == len([card for card in career_cards if location in card.get_position_location()])

    def click_view_role_link(self):
        with self._page.context.expect_page() as new_page_info:
            self.get_career_cards()[0].click_view_role_link()
            self._lever_page = new_page_info.value
            return self._lever_page

    def is_lever_page_opened(self, domain):
        return domain in self._lever_page.url
