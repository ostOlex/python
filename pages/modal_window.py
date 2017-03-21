from pages.base_page import BasePage


class ModalWindow(BasePage):
    def __init__(self):
        self.modal_window = self.driver.find_elements_by_class_name('modal-dialog')

    def fill_in_field_by_name(self, field_name, text):
        text_fields = self.modal_window.find_elements_by_class_name('form-type-textfield')
        for text_field in text_fields:
            # how to do thid in python? I don't remember
            field_label = text_field.find_element_by_tag('label').text
            if field_label.encode("utf-8") == field_name:
                field_label.find_element_by_tag('input').send_keys(text)

    def fill_in_textarea_field_by_name(self, field_name, text):
        textarea_field = self.modal_window.find_elements_by_class_name('form-type-textarea')
        for textarea_field in textarea_field:
            # how to do thid in python? I don't remember
            field_label = textarea_field.find_element_by_tag('label').text
            if field_label.encode("utf-8") == field_name:
                field_label.find_element_by_tag('textarea').send_keys(text)

    def click_submit(self):
        self.modal_window.find_elements_by_class_name('form-submit').click()
   # def select_value_from_dropdown(self):