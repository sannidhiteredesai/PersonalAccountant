from behave import *


@given(u'I am on login page')
def step_impl(context):
    context.browser.get(url='http://127.0.0.1:5000/login')


@given('I enter valid username and password')
def step_impl(context):
    context.browser.find_element_by_name('username').send_keys('validusername')
    context.browser.find_element_by_name('password').send_keys('validpassword')


@given('I enter invalid username or password')
def step_impl(context):
    context.browser.find_element_by_name('username').send_keys('invalidusername')
    context.browser.find_element_by_name('password').send_keys('invalidpassword')


@when('I click on "{button}" button')
def step_impl(context, button):
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='{button}']").click()


@then(u'login is successful')
def step_impl(context):
    assert 'Unable to login, invalid username or password !!' not in context.browser.page_source
    context.browser.find_element_by_xpath('//a[@href="/logout"]').click()


@then(u'login fails')
def step_impl(context):
    alert = context.browser.find_element_by_class_name("alert").text
    assert 'Unable to login, invalid username or password !!' in alert
