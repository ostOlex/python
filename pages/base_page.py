

class BasePage(object):
    def click_on_button_by_name(self, button_name):
        search_button = self.driver.find_element_by_name(button_name)
        search_button.submit()

    def search_by_key(self, key):
        search_box = self.driver.find_element_by_name('query')
        search_box.send_keys(key)

    def is_text_present(self, element, text):
        element_text = element.text
        return text in element_text