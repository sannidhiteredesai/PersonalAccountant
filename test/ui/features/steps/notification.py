from behave import *


@then(u'I see the fds that are maturing till next 45 days')
def step_impl(context):
    assert 3 == context.browser.page_source.count('FD Matured')
