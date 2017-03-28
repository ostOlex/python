from pages.base_page import BasePage
from pages.modal_window import ModalWindow
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions


class DetailsPage(BasePage):
    def get_description_text(self):
        description_element = self.driver.find_element_by_css_selector('.tab-description-text .row')
        return description_element.text

    def get_upper_comments_text(self):
        return self.driver.find_element_by_class_name('review-count').text

    def click_comments_tab(self):
        comment_tab_element = WebDriverWait(self.driver, 20).until(
            ExpectedConditions.element_to_be_clickable((By.CLASS_NAME, "tab-rating")))
        #self.driver.find_element_by_class_name('tab-rating').click()
        self.driver.execute_script("arguments[0].click();", comment_tab_element)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", comment_tab_element)
        #element.click()

    def get_count_of_comments(self):
        return len(self.driver.find_elements_by_class_name('views-row'))

    def get_product_title(self):
        return self.driver.find_element_by_tag_name('h1').text.encode("utf-8")

    def click_add_comment_button(self):
        add_button = WebDriverWait(self.driver, 20).until(
            ExpectedConditions.element_to_be_clickable((By.CLASS_NAME, 'write-review')))
        #self.driver.find_element_by_class_name('write-review').click()
        time.sleep(5)
        add_button.click()
        time.sleep(5)
        return ModalWindow(self.driver)

    def close_sleek_element(self):
        wait = WebDriverWait(self.driver, 300)
        wait.until(ExpectedConditions.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'sleeknote')))
        time.sleep(10)
        #iframe = self.driver.find_elements_by_class_name('sleeknote')[0]
        #self.driver.switch_to_frame(iframe)
        sleek_button_element = WebDriverWait(self.driver, 20).until(
            ExpectedConditions.element_to_be_clickable((By.CLASS_NAME, "SNCloseButton")))
        sleek_button_element = WebDriverWait(self.driver, 20).until(
            ExpectedConditions.visibility_of_element_located((By.CLASS_NAME, "SNCloseButton")))

        #sleeknoteElement
        sleek_button_element.click()
        self.driver.switch_to_default_content()
        time.sleep(10)
