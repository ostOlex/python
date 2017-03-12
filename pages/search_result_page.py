from pages.base_page import BasePage


class SearchResultPage(BasePage):
    def get_products_count(self):
        product_list = self.driver.find_element_by_id("product-list-content")
        products_list = product_list.find_elements_by_class_name('product')
        return len(products_list)
