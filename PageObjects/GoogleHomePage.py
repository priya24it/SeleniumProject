from selenium.webdriver.common.by import By
#from PageObjects.GoogleSearchPage  import SearchPage

from keyboard import press
import keyboard

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    SearchKeyword = (By.CSS_SELECTOR, "input[name='q']")
    SubmitButtonID = (By.XPATH, "//div[@class='tfB0Bf']//input[@name='btnK']")

    def SendKeys(self):
        self.driver.find_element(*HomePage.SearchKeyword).send_keys("Gmail Signin")
        press('enter')
        #SearchPage(self.driver)

    def clickonsubmit(self):
        self.driver.find_element(*HomePage.SubmitButtonID).click()





