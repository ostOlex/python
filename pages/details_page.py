from pages.base_page import BasePage


class DetailsPage(BasePage):
    def get_description_text(self):
        description_element = self.driver.find_element_by_css_selector('.tab-description-text .row')
        return description_element.text

    def get_upper_comments_text(self):
        return self.driver.find_element_by_class_name('review-count').text

    def click_comments_tab(self):
        self.driver.find_element_by_class_name('tab-rating').click

    def get_count_of_comments(self):
        return len(self.driver.find_elements_by_class_name('views-row'))
