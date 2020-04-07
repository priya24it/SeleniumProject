import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from UtilityClass.utilityclass import commonclass



@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("passdictdata")
class SampleTestGmail(commonclass):

    def test_gmail(self,passdictdata):
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
        list = self.driver.find_elements_by_xpath("//div[@id='search']//div[@class='g']//div[@class='r']//h3")
        #print(list.text)
        log.info("total elements s of the .. " + str(len(list)))
        for i in list:
            log.info("entered the loop")
            loopvalue = i.text
            log.info("the first value is ::"+loopvalue)
            if loopvalue in  "Google Login - Sign in - Google Accounts":
                log.info("value has matched...")
                i.click()
                break

                #i.find_elements_by_xpath("//h3").click()
                #break
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR,"span[class='NlWrkb snByac']"))
            #wait = WebDriverWait(self.driver,10)
            #wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,"span[class='NlWrkb snByac']"))
        self.driver.find_element_by_css_selector("span[class='NlWrkb snByac']").click()
        formyself = self.driver.find_element_by_xpath("//div[@class='XvhY1d']//div/span[1]")
        log.info("formyself element"+formyself.text)
        formyself.click()
        log.info(self.driver.title)


        window_after = self.driver.window_handles[0]
        self.driver.switch_to.window(window_after)
        time.sleep(10)

        window_after_title = self.driver.title
        log.info(window_after_title)

        #firstName = self.driver.find_element_by_xpath("//input[@id='firstName']").click()
        #self.driver.find_element_by_xpath("//input[@id='firstName']").send_keys("h17845")
        self.driver.find_element_by_xpath("//input[@id='firstName']").send_keys(passdictdata[0])
        self.driver.find_element_by_xpath("//input[@id='lastName']").send_keys(passdictdata[1])
        self.driver.find_element_by_xpath("//input[@id='username']").send_keys(passdictdata[2])
        self.driver.find_element_by_xpath("//input[@name='Passwd']").send_keys(passdictdata[3])
        self.driver.find_element_by_xpath("//input[@name='ConfirmPasswd']").send_keys(passdictdata[4])
        self.driver.find_element_by_xpath("//span[@class='CwaK9']").click()

        window_after = self.driver.window_handles[0]
        self.driver.switch_to.window(window_after)
        time.sleep(10)
        window_after_title = self.driver.title
        log.info(window_after_title)
        log.info(self.driver.current_url)

        h1value = self.driver.find_element_by_xpath("//h1[@class='sfYUmb']").text
        log.info("Final Text value::" + h1value)
        self.driver.find_element_by_xpath("//input[@id='phoneNumberId']").send_keys("12345")
        time.sleep(6)
        FinalTextvalue = self.driver.find_element_by_xpath("//input[@id='phoneNumberId']").text
        log.info("Final Text value::" + FinalTextvalue)
        assert "Verifying your phone number" in h1value , "Both are matching"












        #self.driver.close()
