from time import sleep
from behave import *
from selenium import webdriver


@given("Launch Browser")
def launch_browser(context):
    context.driver=webdriver.Chrome()

@when("Navigate To Url")
def navigate_to_url(context):
    context.driver.get("https://demowebshop.tricentis.com/")
@when("Maximize browser")
def maximize_browser(context):
    context.driver.maximize_window()

@when("Validate home page")
def validate_home_page_with_logo(context):
    status=context.driver.find_element("xpath",'//div[@class="header-logo"]').is_displayed()
    assert status==True
@when("Click On Login Button")
def click_on_login_button(context):
    context.driver.find_element('xpath','//a[text()="Log in"]').click()

@when('Enter username "{user}" and password "{passwords}"')
def enter_username_password(context,user,passwords):
    context.driver.find_element('id',"Email").send_keys(user)
    context.driver.find_element('id',"Password").send_keys(passwords)
@when('Click On Submit Button')
def click_on_submit_button(context):
    context.driver.find_element('xpath','//input[@class="button-1 login-button"]').click()
    sleep(2)
@then('Validate with logout button')
def validateWithLogoutButton(context):
    try:
        # Check if "Log out" button is displayed after successful login
        logout_button = context.driver.find_element('xpath', '//a[text()="Log out"]')
        assert True,"Test Passed"
        # print("*********Test passed:******** Logout button is visible.*********")
        sleep(2)
    except Exception as e:
        fstatus = context.driver.find_element('xpath',"//span[contains(text(),'Login was unsuccessful')]").is_displayed()
        # assert fstatus
        assert False,"Test Failed"
        # print("*********Test Failled*******: Logout button is not visible.********")


@then("close browser")
def close_browser(context):
    context.driver.close()

