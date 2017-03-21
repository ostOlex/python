from pages.base_page import BasePage
from pages.modal_window import ModalWindow
import time


class DetailsPage(BasePage):
    def get_description_text(self):
        description_element = self.driver.find_element_by_css_selector('.tab-description-text .row')
        return description_element.text

    def get_upper_comments_text(self):
        return self.driver.find_element_by_class_name('review-count').text

    def click_comments_tab(self):
        self.driver.find_element_by_class_name('tab-rating').click()

    def get_count_of_comments(self):
        return len(self.driver.find_elements_by_class_name('views-row'))

    def get_product_title(self):
        return self.driver.find_element_by_tag_name('h1').text.encode("utf-8")

    def click_add_comment_button(self):
        self.driver.find_element_by_class_name('write-review').click()
        time.sleep(5)
        return ModalWindow(self.driver)
