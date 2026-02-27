from components.career_card_component import CareerCardComponent
from pages.base_page import BasePage
from playwright.sync_api import Page


class OpenPositionsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.filter_location_dropdown = page.locator("#filter-by-location")
        self.filter_department_dropdown = page.locator("#filter-by-department")
        self.career_position_list = page.locator("#jobs-list")
        self.no_jobs_label = page.locator(".no-job-result")

    def filter_location(self, location: str):
        self.filter_location_dropdown.select_option(label=location)

    def filter_department(self, department):
        self.filter_department_dropdown.select_option(label=department)

    def get_career_cards(self) -> list[CareerCardComponent]:
        cards_locator = self.career_position_list.locator(".position-list-item")
        return [
            CareerCardComponent(self._page, cards_locator.nth(i))
            for i in range(cards_locator.count())
        ]

    def click_view_role_link(self):
        self.get_career_cards()[0].click_view_role_link()

    def get_position_list_inner_html(self):
        return self.career_position_list.inner_html()

    def wait_until_jobs_updated(self, old_state, timeout=10000):
        self._page.wait_for_function(
            """
            (oldState) => {
                const el = document.querySelector("#jobs-list");
                return el && el.innerHTML !== oldState;
            }
            """,
            arg=old_state,
            timeout=timeout
        )


