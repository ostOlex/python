from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage



class HomePage(BasePage):
    def __init__(self, webdriver):
        self.driver = webdriver

    def click_sarch_button(self):
        self.click_on_button_by_name('op')
        return SearchResultPage(self.driver)