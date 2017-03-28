from pages.base_page import BasePage
import time


class ModalWindow(BasePage):
    def __init__(self, webdriver):
        self.driver = webdriver
        self.modal_window = self.driver.find_element_by_class_name('modal-dialog')

    def fill_in_field_by_name(self, field_name, text):
        text_fields = self.modal_window.find_elements_by_class_name('form-type-textfield')
        for text_field in text_fields:
            # how to do this in python? I don't remember
            input_element = text_field.find_element_by_class_name('form-text')
            field_label = input_element.get_attribute("placeholder")
            if field_name in field_label.encode("utf-8"):
                input_element.send_keys(text)
                return

    def fill_in_textarea_field_by_name(self, field_name, text):
        textarea_field = self.modal_window.find_elements_by_class_name('form-type-textarea')
        for textarea_field in textarea_field:
            # same
            textarea_element = textarea_field.find_element_by_class_name('form-textarea')
            field_label = textarea_element.get_attribute("placeholder")
            if field_name in field_label.encode("utf-8") :
                textarea_element.send_keys(text)
                return

    def click_rating_star(self):
        self.modal_window.find_element_by_class_name('rating').find_element_by_class_name('star-2').click()

    def is_validation_error_present(self):
       return self.modal_window.find_element_by_class_name('validation-failed').is_displayed()

    def click_submit(self):
        self.modal_window.find_element_by_class_name('form-submit').click()
        time.sleep(5)
