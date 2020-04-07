import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.GoogleAssertPage import AssertPage
from UtilityClass.utilityclass import commonclass


class CreateAccount(commonclass):

    def __init__(self,driver):
        self.driver = driver

    nextButton = (By.XPATH , "//span[@class='CwaK9']")
    firstName = (By.XPATH, "//input[@id='firstName']")
    lastName = (By.XPATH, "//input[@id='lastName']")
    username = (By.XPATH, "//input[@id='username']")
    Passwd = (By.XPATH, "//input[@name='Passwd']")
    ConfirmPasswd = (By.XPATH, "//input[@name='ConfirmPasswd']")


    @pytest.mark.usefixtures("passdata")
    def createaccountwithtestdata(self):
        global log
        log = self.getLogger()
        log.info("method is createaccountwithtestdata")
        log.info(self.driver.current_url)
        time.sleep(3)
        self.driver.find_element(*CreateAccount.firstName).send_keys("TimeosfIndal")
        self.driver.find_element(*CreateAccount.lastName).send_keys("TimeosfIndal")
        self.driver.find_element(*CreateAccount.username).send_keys("TimeosfIndal18India")
        self.driver.find_element(*CreateAccount.Passwd).send_keys("DeccanChornical@12345")
        self.driver.find_element(*CreateAccount.ConfirmPasswd).send_keys("DeccanChornical@12345")
        self.driver.find_element(*CreateAccount.nextButton).click()
        return AssertPage(self.driver)



