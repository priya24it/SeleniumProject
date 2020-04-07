import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.GoogleSigninPage import Signinpage
from UtilityClass.utilityclass import commonclass


class SearchPage(commonclass):

    def __init__(self,driver):
        self.driver = driver

    list1 = (By.XPATH , "//div[@id='search']//div[@class='g']//div[@class='r']//h3")

    def ClickonSigninLink(self):
        global log
        log = self.getLogger()
        list = self.driver.find_elements(*SearchPage.list1)
        log.info("total elements s of the .. " + str(len(list)))
        for i in list:
            log.info("entered the loop")
            loopvalue = i.text
            log.info("the first value is ::" + loopvalue)
            if loopvalue in "Google Login - Sign in - Google Accounts":
                log.info("value has matched...")
                i.click()
                break
        return Signinpage(self.driver)


