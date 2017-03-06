from pages.base_page import BasePage

class DetailsPage(BasePage):
    def __init__(self, webdriver):
        self.driver = webdriver

    def get_description_text(self):
        description_element = self.driver.find_element_by_css_selector('.tab-description-text .row')
        return description_element.text