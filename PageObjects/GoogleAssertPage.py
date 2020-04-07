import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.GoogleHomePage import HomePage
from UtilityClass.utilityclass import commonclass


class AssertPage(commonclass):

    def __init__(self,driver):
        self.driver = driver

    h1Text = (By.XPATH , "//h1[@class='sfYUmb']")
    PhoneNumber = (By.XPATH, "//input[@id='phoneNumberId']")

    def Clickonassertpage(self):
        global log
        log = self.getLogger()
        time.sleep(2)
        log.info(self.driver.current_url)
        self.driver.find_element(*AssertPage.PhoneNumber).send_keys("12345")
        h1value = self.driver.find_element(*AssertPage.h1Text).text
        log.info("Final Text value::" + h1value)
        return h1value
