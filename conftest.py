import pytest
from playwright.sync_api import Page

from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.open_positions_page import OpenPositionsPage


@pytest.fixture(autouse=True)
def set_default_timeout(page: Page):
    page.set_default_timeout(120000)

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page=page)

@pytest.fixture
def careers_page(page: Page) -> CareersPage:
    return CareersPage(page=page)

@pytest.fixture
def open_positions_page(page: Page) -> OpenPositionsPage:
    return OpenPositionsPage(page=page)


