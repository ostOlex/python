from pages.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, webdriver):
        self.driver = webdriver

    def get_products_count(self):
        product_list = self.driver.find_element_by_css_selector("[class = 'products row']")
        products_list = product_list.find_elements_by_class_name('col-xs-12')
        return len(products_list)
