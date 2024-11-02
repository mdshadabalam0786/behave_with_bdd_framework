from features.lib.BasePage import SeleniumWrapper
class HomePage(SeleniumWrapper):
    def __init__(self,driver):
        super().__init__(driver)
    search_option_on_home_page_xpath='//input[@name="search"]'
    search_button_on_home_page_xpath='//button[@class="btn btn-default btn-lg"]'

    def send_value_on_search(self,product):
        self.send_value_on_element("xpath",self.search_option_on_home_page_xpath,product)
    def click_on_search_button(self):
        self.click_on_element('xpath',self.search_button_on_home_page_xpath)
