from behave import *
from selenium import webdriver


use_step_matcher("re")


@given('the Springer homepage is not loaded')
def step_impl(context):
    context.driver = webdriver.Chrome("C:\\Users\\worre\\AppData\\Local\\webdrivers\\chromedriver.exe")
    context.driver.get("http://www.google.co.uk")


@given('the Springer home is loaded')
def step_impl(context):
    context.driver = webdriver.Chrome("C:\\Users\\worre\\AppData\\Local\\webdrivers\\chromedriver.exe")
    context.driver.get("https://link.springer.com")


@when('the Springer homepage is loaded')
def step_impl(context):
    context.driver.get("https://link.springer.com/")


@when('the term permissive hypotension is searched for')
def step_impl(context):
    context.elem = context.driver.find_elements_by_xpath("//title[contains(@title, 'Search')]")
    context.elem.clear()
    context.elem.send_keys('permissive hypotension')
    pass


@then('the Search box is present')
def step_impl(context):
    context.driver.find_elements_by_xpath("//title[contains(@name, 'query')]")
    pass


@then('the {results} are returned')
def step_impl(context):
    context.driver.find_elements_by_xpath("//*[contains(text(), results)]")
    pass


@then('the results for permissive hypotension are returned')
def step_impl(context):
    context.driver.find_elements_by_xpath("//*[contains(text(), '1,872')]")
    pass
