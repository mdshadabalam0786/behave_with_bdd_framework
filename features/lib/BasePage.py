class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver
    def click_on_element(self,loc,loc_value):
        self.driver.find_element(loc,loc_value).click()
    def send_value_on_element(self,loc,loc_value,value):
        self.driver.find_element(loc,loc_value).send_keys(value)