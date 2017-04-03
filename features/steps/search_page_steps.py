from behave import *


@then('I check is search result contain 8 products')
def check_is_product_count(context):
    assert context.search_result_page.get_products_count() == 8