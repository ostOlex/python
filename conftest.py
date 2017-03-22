import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver_fixture():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='C:\Python27\chromedriver-Windows', chrome_options=options)
    driver.get('https://jysk.ua/vitalnya-stolova/obidniy-nabir/stil-ryslinge-4-stilci-ryslinge');
    time.sleep(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def main_driver_fixture():
    driver = webdriver.Chrome('C:\Python27\chromedriver-Windows')
    driver.get('https://jysk.ua/');
    time.sleep(5)
    yield driver
    driver.quit()
