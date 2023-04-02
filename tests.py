import pytest
from playwright.sync_api import Page


URL = 'https://picfinder.ai/'
SELECTORS = {'search_bar': '#form-search-bar\[search-box\]',
             'spiners': '.grid-wrapper > div > .s-result-grid-item > .s-result-grid-item-hover'}
STRINGS = {'motto': 'Infinite image generation powered by AI.',
           'copywright': 'Copyright © 2023 PicFinder.ai All rights reserved.',
           'donate': 'Your generosity keeps us going.',
           'in_touch': 'Get in touch',
           'images_generated': 'Images Generated:'}
DEFAULT_TIMEOUT = 3000


def test_landing_page(page: Page) -> None:
    page.set_default_timeout(DEFAULT_TIMEOUT)
    page.goto(URL)
    search_bar = page.query_selector(SELECTORS['search_bar'])
    assert 'Try ' in search_bar.get_attribute('placeholder')
    page.get_by_role("heading").click()
    page.get_by_text(STRINGS['motto']).click()
    page.get_by_text(STRINGS['images_generated']).click()
    page.get_by_role("contentinfo").get_by_text(STRINGS['copywright']).click()
    page.get_by_role("contentinfo").get_by_text(STRINGS['donate']).click()
    page.get_by_role("link", name="DONATE").click()
    page.get_by_role("dialog").click()
    page.get_by_role("link", name=STRINGS['in_touch']).press("Escape")


@pytest.hookimpl(hookwrapper=True)
@pytest.mark.parametrize("search_string", ['doodooo'])
def test_search(search_string, page: Page) -> None:
    page.set_default_timeout(DEFAULT_TIMEOUT)
    page.goto(URL)
    search_bar = page.wait_for_selector(SELECTORS['search_bar'])
    search_bar.type(search_string)
    page.locator("#aux-buttons").get_by_role("link").click()
    results = page.wait_for_selector('.s-result')
    assert results is not None
    results_section = page.wait_for_selector('.grid-wrapper')
    assert results_section is not None
    page.wait_for_selector(SELECTORS['spiners']).is_visible()

