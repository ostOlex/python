import time


class BasePage(object):
    def __init__(self, webdriver):
        self.driver = webdriver

    def click_on_button_by_name(self, button_name):
        search_button = self.driver.find_element_by_name(button_name)
        search_button.submit()

    def search_by_text(self, text):
        search_box = self.driver.find_element_by_name('query')
        search_box.send_keys(text)
        self.click_on_button_by_name('op')
        time.sleep(5)

    def is_text_present(self, element, text):
        element_text = element.text
        return text in element_text