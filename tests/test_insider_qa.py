from configs.settings import HOME_PAGE_URL, QA_CAREERS_URL
from utils.config_utils import get_test_data


LOCATION = get_test_data("location")
DEPARTMENT = get_test_data("department")
TITLE = get_test_data("job_title")
LEVER_DOMAIN = get_test_data("lever_domain")


class TestInsiderQA:
    def test_insider_qa(self, home_page, careers_page, open_positions_page):
        home_page.visit(HOME_PAGE_URL)
        assert home_page.is_page_opened(HOME_PAGE_URL), "Home page is not opened"
        home_page.accept_all_cookies()
        assert home_page.is_header_present(), "Header is not present"
        assert home_page.is_main_sections_present(), "Main sections are not present"
        assert home_page.is_footer_present(), "Footer is not present"

        careers_page.visit(QA_CAREERS_URL)
        assert careers_page.is_page_opened(QA_CAREERS_URL), "Careers page is not opened"
        careers_page.click_see_all_qa_jobs_button()

        open_positions_page.filter_location(LOCATION)
        open_positions_page.filter_department(DEPARTMENT)
        assert open_positions_page.get_career_cards(), "Career cards are not present"
        assert open_positions_page.is_cards_title_match(TITLE), "Career cards title doesn't match"
        assert open_positions_page.is_cards_department_match(DEPARTMENT), "Career cards department doesn't match"
        assert open_positions_page.is_cards_location_match(LOCATION), "Career cards location doesn't match"

        open_positions_page.click_view_role_link()
        assert open_positions_page.is_lever_page_opened(LEVER_DOMAIN), "Lever page is not opened"









