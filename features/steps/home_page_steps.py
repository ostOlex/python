from behave import *


@then('I search item by "RYSLINGE" text')
def search_item_by_text(context):
   context.search_result_page = context.home_page.search_item_by_text('RYSLINGE')