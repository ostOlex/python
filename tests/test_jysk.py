from pages.home_page import HomePage


def test_test(main_driver_fixture):
    home_page = HomePage(main_driver_fixture)
    search_result_page = home_page.search_item_by_text('RYSLINGE')
    assert search_result_page.get_products_count() == 8

