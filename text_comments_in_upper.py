import pytest
from selenium import webdriver
import time
from pages.details_page import DetailsPage


@pytest.fixture(scope="module")
def driver_fixture():
    driver = webdriver.Chrome('C:\Python27\chromedriver-Windows')
    driver.get('https://jysk.ua/vitalnya-stolova/obidniy-nabir/stil-ryslinge-4-stilci-ryslinge');
    time.sleep(5)
    yield driver
    driver.quit()


def test_description(driver_fixture):
    details_page = DetailsPage(driver_fixture)
    #assert that page contains 4 comments in upper
    assert '4' in details_page.get_upper_comments_text()