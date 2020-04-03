import pytest
#import CommonClass
import time


@pytest.mark.usefixtures("setup")
class TestGmail:

    def test_gmail(self):
        log = self.getLogger()
        log.debug('hello')
        self.driver.find_element_by_css_selector("input[name='q']").send_keys("Gmail Signin")
        #searchkeyword = self.driver.find_elements_by_xpath("//div[@id='realbox-matches']//a")
        searchkeyword = self.driver.find_elements_by_xpath("//ul[@class ='erkvQe']//li")
        log.info("length of the .. "+str(len(searchkeyword)))
        for i in range(0,len(searchkeyword)):
            log.info(i)
        time.sleep(3)
        #self.driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']").click()
        self.driver.find_element_by_xpath("//div[@class ='tfB0Bf']//input[@name='btnK']").click()
       # self.driver.find_element_by_css_selector("//h3[contains(text(),'Google Login - Sign in - Google Accounts')]").Click()
        list = self.driver.find_elements_by_xpath("//div[@id='search']//div[@class='g']//div[@class='r']")
        log.info("total elements s of the .. " + str(len(list)))
        for i in list:
            log.info(i.text)
            if i == "Google Login - Sign in - Google Accounts":
                i.click()


        #self.driver.close()
