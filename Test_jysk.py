from selenium import webdriver
from pages.home_page import HomePage
import time


class Test_jysk:
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome('C:\Python27\chromedriver-Windows')
        self.driver.get('https://jysk.ua/');
        time.sleep(5)

    def test_test(self):
        home_page = HomePage(self.driver)
        search_result_page = home_page.search_item_by_text('RYSLINGE')
        #dropdown_menu = self.driver.find_element_by_class_name('dropdown-menu')
        #result_items = dropdown_menu.find_elements_by_class_name('search-suggestion')
        #assert len(result_items) == 7
        assert search_result_page.get_products_count() == 8

    @classmethod
    def teardown_class(self):
        self.driver.quit()
