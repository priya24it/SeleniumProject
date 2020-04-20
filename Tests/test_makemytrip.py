from selenium import webdriver
import pytest
import time

@pytest.mark.usefixtures("setup")
class Testmakymytrip:
    def test_trip(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'From')]").click()
        listofelements = self.driver.find_elements_by_xpath("//ul[contains(@class,'react-autosuggest__suggestions-list')]//li")
        print(len(listofelements))
        for i in range(0,len(listofelements)):
            print(listofelements[i].text)
            #print(i)
            if(str(listofelements[i].text).__contains__("Hyderabad, India")):
                listofelements[i].click()
                break;
        time.sleep(4)
        self.driver.find_element_by_xpath("//span[contains(text(),'To')]").click()
        listofelements = self.driver.find_elements_by_xpath("//ul[contains(@class,'react-autosuggest__suggestions-list')]//li")
        print(len(listofelements))
        for i in range(0, len(listofelements)):
            print(listofelements[i].text)
            # print(i)
            if (str(listofelements[i].text).__contains__("London")):
                listofelements[i].click()
                break;
        time.sleep(4)
        self.driver.find_element_by_xpath("//div[contains(@class,'fsw_inputBox dates inactiveWidget')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(@class,'DayPicker-wrapper')]//div[1]//div[3]//div[4]//div[5]//div[1]//p[1]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//p[contains(@class,'latoBlack font12 greyText')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(@class,'DayPicker-Months')]//div[2]//div[3]//div[1]//div[6]//div[1]//p[1]").click()
        time.sleep(5)







        self.driver.close()