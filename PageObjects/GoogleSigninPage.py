import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.GoogleCreateAccount import CreateAccount
from UtilityClass.utilityclass import commonclass


class Signinpage(commonclass):

    def __init__(self,driver):
        self.driver = driver

    createAccountLink = (By.CSS_SELECTOR , "span[class='NlWrkb snByac']")
    formmyself = (By.XPATH, "//div[@class='XvhY1d']//div/span[1]")

    def Clickoncreateaccountlink(self):
        global log
        log = self.getLogger()
        log.info(self.driver.current_url)
        time.sleep(3)
        self.driver.find_element(*Signinpage.createAccountLink).click()
        formyself = self.driver.find_element(*Signinpage.formmyself)
        log.info("formyself element" + formyself.text)
        formyself.click()
        log.info("formyself element has cliked")
        return CreateAccount(self.driver)
