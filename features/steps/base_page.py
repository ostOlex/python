import time
from behave import *


class BasePage(object):
    def __init__(self, webdriver):
        self.driver = webdriver

    @then('I click on button with name {button_name}')
    def click_on_button_by_name(self, button_name):
        search_button = self.driver.find_element_by_name(button_name)
        search_button.submit()

    @then('I search by "{text}" text')
    def search_by_text(self, text):
        search_box = self.driver.find_element_by_name('query')
        search_box.send_keys(text)
        self.click_on_button_by_name('op')
        time.sleep(5)

    @then('I check is element "{element}" with "{text}" text is present')
    def is_text_present(self, element, text):
        element_text = element.text
        return text in element_text