from selenium import webdriver
from utilities import ConfigReader
def before_scenario(context,driver):
    print("before scenario got called")
    browser=ConfigReader.read_configuration("basic info","browser")
    if browser=='chrome':
        context.driver = webdriver.Chrome()
    elif browser=='firefox':
        context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(20)
def after_scenario(context,driver):
    print("after scenario got called")
    context.driver.close()