from behave import *


@then('I check is text "входять 2 додаткових \"крила\" is present')
def check_is_text_present(context):
    text = u"входять 2 додаткових \"крила\"."
    assert text in context.details_page.get_description_text()