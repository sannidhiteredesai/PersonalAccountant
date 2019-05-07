from behave import *


@given(u'I navigate to "{this}" page')
@when(u'I navigate to "{this}" page')
def step_impl(context, this):
    context.browser.get(url='http://127.0.0.1:5000/' + this)


@when('I click on "{button}" button')
def step_impl(context, button):
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='{button}']").click()
