from time import sleep
from behave import *
from utilities import ConfigReader
@given(u'I Navigate to home page')
def step_impl(context):
    context.driver.get(ConfigReader.read_configuration("basic info","url"))
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
@when(u'I click on my account button on homepage')
def step_impl(context):
    context.driver.find_element("xpath",'//span[text()="My Account"]').click()


@when(u'I click on register button')
def step_impl(context):
    context.driver.find_element("xpath",'//a[text()="Register"]').click()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        context.driver.find_element('id',"input-firstname").send_keys(row['first_name'])
        context.driver.find_element('id', "input-lastname").send_keys(row['last_name'])
        context.driver.find_element('id', "input-email").send_keys(row['email'])
        context.driver.find_element('id', "input-telephone").send_keys(row['mobile'])
        context.driver.find_element('id', "input-password").send_keys(row['password'])
        context.driver.find_element('id', "input-confirm").send_keys("confirm_password")
        context.driver.find_element('css selector','input[value="Continue"]').click()
        sleep(5)



@then(u'Account should get created')
def step_impl(context):
    pass
