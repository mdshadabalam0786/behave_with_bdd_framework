from time import sleep
from features.pages.home_pages import HomePage
from utilities import ConfigReader
from behave import *





@Given("I Launch The Browser")
def launching_the_browser(context):
    print("launch browser got called")
@When("I Navigate to Url on Home pages")
def navigateing_to_url_on_home_page(context):
    context.driver.get(ConfigReader.read_configuration("basic info","url"))
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)

@When('I Enter valid product "{prod}" On Search Input Box')
def addValidProduct(context,prod):
    context.home_page=HomePage(context.driver)
    context.home_page.send_value_on_search(prod)

@When('I Enter invalid product "{products}" On Search Input Box')
def addInValidProduct(context,products):
    context.driver.find_element("xpath",'//input[@name="search"]').send_keys(products)

@When("I Click On Search Button")
def click_on_search_button(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_search_button()

    sleep(5)
@Then("Validate the product Should get displayed in list")
def validateList(context):
    try:
        a=context.driver.find_element('xpath','//a[text()="HP LP3065"]').text
        assert a=="HP LP3065"
    except:
        assert False,"Test Failed"
@Then("I close browser")
def close_browser(context):
    print("close browser got called")