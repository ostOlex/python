from selenium import webdriver
import time

class Test_jysk:

    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome('C:\Python27\chromedriver-Windows')
        self.driver.get('https://jysk.ua/');
        time.sleep(5)

    def test_test(self):
        search_box = self.driver.find_element_by_name('query')
        search_box.send_keys('RYSLINGE')
        time.sleep(5)
        #dropdown_menu = self.driver.find_element_by_class_name('dropdown-menu')
        #result_items = dropdown_menu.find_elements_by_class_name('search-suggestion')
        #assert len(result_items) == 7

        search_button = self.driver.find_element_by_name('op')
        search_button.submit()
        time.sleep(5)

        product_list = self.driver.find_element_by_css_selector("[class = 'products row']")
        products_list = product_list.find_elements_by_class_name('col-xs-12')
        assert len(products_list) == 8

    @classmethod
    def teardown_class(self):
        self.driver.quit()
