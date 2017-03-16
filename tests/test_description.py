# -*- coding: utf-8 -*-
from pages.details_page import DetailsPage


def test_description(driver_fixture):
    details_page = DetailsPage(driver_fixture)
    text = u"входять 2 додаткових \"крила\"."
    assert text in details_page.get_description_text()