import pytest
import time
from selenium.common.exceptions import NoSuchElementException

def test_open_link_different_languages (browser):
    try:
        button = len (browser.find_elements_by_css_selector(".btn-add-to-basket"))
        assert button > 0, "Missing element on page"         
    except NoSuchElementException:
        pass
    time.sleep(5)