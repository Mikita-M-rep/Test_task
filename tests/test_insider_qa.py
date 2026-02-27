from playwright.sync_api import expect
from configs.settings import HOME_PAGE_URL, QA_CAREERS_URL
from pages.lever_page import LeverPage
from utils.config_utils import get_test_data

LOCATION = get_test_data("location")
DEPARTMENT = get_test_data("department")
TITLE = get_test_data("job_title")
LEVER_DOMAIN = get_test_data("lever_domain")


def test_insider_qa(home_page, careers_page, open_positions_page):
    home_page.visit(HOME_PAGE_URL)
    assert home_page.is_page_opened(HOME_PAGE_URL), "Home page is not opened"
    home_page.accept_all_cookies()
    assert home_page.is_header_present(), "Header is not present"
    assert home_page.is_main_sections_present(), "Main sections are not present"
    assert home_page.is_footer_present(), "Footer is not present"

    careers_page.visit(QA_CAREERS_URL)
    assert careers_page.is_page_opened(QA_CAREERS_URL), "Careers page is not opened"
    careers_page.click_see_all_qa_jobs_button()

    expect(open_positions_page.filter_location_dropdown).to_contain_text(LOCATION, timeout=120000)
    initial_load = open_positions_page.get_position_list_inner_html()
    open_positions_page.wait_until_jobs_updated(initial_load, timeout=20000)
    before_filtering = open_positions_page.get_position_list_inner_html()
    open_positions_page.filter_location(LOCATION)
    open_positions_page.filter_department(DEPARTMENT)
    open_positions_page.wait_until_jobs_updated(before_filtering, timeout=20000)

    if not open_positions_page.get_career_cards():
        assert open_positions_page.get_career_cards(), "Career cards are not present"
    for index, card in enumerate(open_positions_page.get_career_cards(), start=1):
        assert TITLE in card.get_position_title(), f"Card #{index} title '{card.get_position_title()}' doesn't contain '{TITLE}'"
        assert DEPARTMENT in card.get_position_department(), f"Card #{index} title '{card.get_position_department()}' doesn't contain '{DEPARTMENT}'"
        assert LOCATION in card.get_position_location(), f"Card #{index} title '{card.get_position_location()}' doesn't contain '{LOCATION}'"

    with open_positions_page.context.expect_page() as page_info:
        open_positions_page.click_view_role_link()
    lever_page = LeverPage(page_info.value)

    assert lever_page.is_page_opened(LEVER_DOMAIN), "Lever page is not opened"
