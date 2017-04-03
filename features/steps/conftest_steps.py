import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from behave import *
from pages.details_page import DetailsPage
from pages.home_page import HomePage


@given("I open browser at details page")
def driver_fixture(context):
    options = Options()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(executable_path='C:\Python27\chromedriver-Windows', chrome_options=options)
    context.driver.get('https://jysk.ua/vitalnya-stolova/obidniy-nabir/stil-ryslinge-4-stilci-ryslinge');
    context.details_page = DetailsPage(context.driver)
    time.sleep(5)
    yield context.driver
    context.driver.quit()


@given("I open browser at home page")
def main_driver_fixture(context):
    context.driver = webdriver.Chrome('C:\Python27\chromedriver-Windows')
    context.driver.get('https://jysk.ua/');
    context.home_page = HomePage(context.driver)
    time.sleep(5)
    yield context.driver
    context.driver.quit()
