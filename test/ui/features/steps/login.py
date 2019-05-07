from behave import *
from selenium.common.exceptions import NoSuchElementException


@given('I enter valid username and password')
def step_impl(context):
    context.browser.find_element_by_name('username').send_keys('validusername')
    context.browser.find_element_by_name('password').send_keys('validpassword')


@given('I enter invalid username or password')
def step_impl(context):
    context.browser.find_element_by_name('username').send_keys('invalidusername')
    context.browser.find_element_by_name('password').send_keys('invalidpassword')


@then(u'login is successful')
def step_impl(context):
    assert 'Unable to login, invalid username or password !!' not in context.browser.page_source
    context.browser.find_element_by_xpath('//a[@href="/logout"]').click()


@then(u'login fails')
def step_impl(context):
    alert = context.browser.find_element_by_class_name("alert").text
    assert 'Unable to login, invalid username or password !!' in alert


def xpath_exists(context, xpath):
    try:
        context.browser.find_element_by_xpath(xpath)
        return True
    except NoSuchElementException as e:
        return False


@given(u'I am a logged in user')
def step_impl(context):
    context.browser.get(url='http://127.0.0.1:5000/login')
    if not xpath_exists(context, xpath='//a[@href="/logout"]'):
        context.browser.find_element_by_name('username').send_keys('validusername')
        context.browser.find_element_by_name('password').send_keys('validpassword')
        context.browser.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()
