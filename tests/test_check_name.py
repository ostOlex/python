# -*- coding: utf-8 -*-
from pages.home_page import HomePage


def test_check_name(main_driver_fixture):
    home_page = HomePage(main_driver_fixture)
    search_result_page = home_page.search_item_by_text('RYSLINGE')
    #dropdown_menu = self.driver.find_element_by_class_name('dropdown-menu')
    #result_items = dropdown_menu.find_elements_by_class_name('search-suggestion')
    #assert len(result_items) == 7
    product_name = "Стіл RYSLINGE + 4 стільці RYSLINGE"
    details_page = search_result_page.click_on_product_by_name(product_name)
    assert unicode(details_page.get_product_title(), 'utf-8') == unicode(product_name, 'utf-8')
