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
        home_page.search_by_key('RYSLINGE')
        #search_box = self.driver.find_element_by_name('query')
        #search_box.send_keys('RYSLINGE')
        time.sleep(5)
        #dropdown_menu = self.driver.find_element_by_class_name('dropdown-menu')
        #result_items = dropdown_menu.find_elements_by_class_name('search-suggestion')
        #assert len(result_items) == 7

        search_result_page = home_page.click_sarch_button()
        #search_button = self.driver.find_element_by_name('op')
        #search_button.submit()
        time.sleep(5)

        #search_result_page.get_products_count()
       # product_list = self.driver.find_element_by_css_selector("[class = 'products row']")
        #products_list = product_list.find_elements_by_class_name('col-xs-12')
        assert search_result_page.get_products_count() == 8

    @classmethod
    def teardown_class(self):
        self.driver.quit()
