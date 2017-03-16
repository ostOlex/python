from pages.details_page import DetailsPage


def test_description(driver_fixture):
    details_page = DetailsPage(driver_fixture)
    #assert that page contains 4 comments in upper
    assert '4' in details_page.get_upper_comments_text()