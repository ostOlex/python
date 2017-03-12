from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage


class HomePage(BasePage):
    def search_item_by_text(self, text):
        self.search_by_text(text)
        return SearchResultPage(self.driver)#need help with this


    def click_sarch_button(self):
        self.click_on_button_by_name('op')
        return SearchResultPage(self.driver)