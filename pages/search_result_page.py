from pages.base_page import BasePage
from pages.details_page import DetailsPage
from selenium.common.exceptions import NoSuchElementException
import time


class SearchResultPage(BasePage):
    def get_products_count(self):
        product_list = self.driver.find_element_by_id("product-list-content")
        products_list = product_list.find_elements_by_class_name('product')
        return len(products_list)

    def click_on_product_by_name(self, product_name):
        product_elements_list = self.driver.find_elements_by_class_name('product-content')
        for product_element in product_elements_list:
            product_element_name = product_element.find_element_by_class_name('product-name').text
            if product_element_name.encode("utf-8") == product_name:
                product_element.find_element_by_tag_name('a').click
                time.sleep(5)
                return DetailsPage(self.driver)

        raise NoSuchElementException("Product with '{0}' name was not found".format(product_name))