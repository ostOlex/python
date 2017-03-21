# -*- coding: utf-8 -*-
from pages.details_page import DetailsPage


def test_add_new_comment(driver_fixture):
    details_page = DetailsPage(driver_fixture)
    details_page.click_comments_tab()
    modal_window = details_page.click_add_comment_button()
    modal_window.fill_in_field_by_name('Тема', 'qweqe')
    modal_window.fill_in_field_by_name('Ім\'я', 'qweqe')
    modal_window.fill_in_field_by_name('Місто', 'qweqe')
    modal_window.fill_in_field_by_name('Email', 'qweqe')
    modal_window.fill_in_textarea_field_by_name('Відгук', 'wadsf')



