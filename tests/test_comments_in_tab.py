from pages.details_page import DetailsPage


def test_description(driver_fixture):
    details_page = DetailsPage(driver_fixture)
    details_page.click_comments_tab()
    #assert that page contains 4 comments in upper
    assert 4 == details_page.get_count_of_comments()