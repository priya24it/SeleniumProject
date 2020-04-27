import pandas as pd
import pytest
import time
from Tests.conftest import passdictdata


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("passexceldata")
@pytest.mark.skip
class TestDDT:
    def test_ddt(self,passexceldata):
        sourceDF = pd.read_excel('Tests//DDT.xlsx')
        sourceDF = pd.DataFrame(sourceDF)

        print(self.driver.current_url)
        print(passexceldata['username'])
        print(passexceldata['password'])
        self.driver.find_element_by_xpath("//input[@id='login_field']").send_keys(passexceldata['username'])
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys(passexceldata['password'])
        self.driver.find_element_by_xpath("//input[@name='commit']").click()
        title = self.driver.title
        print("Title = " + title)
        time.sleep(3)
        if title  == "GitHub":
            sourceDF["result"] = 'pass'
            assert "GitHub" in title, "passed"
            self.driver.find_element_by_xpath("//details[@class ='details-overlay details-reset js-feature-preview-indicator-container']//summary[@ class ='Header-link']").click()
            self.driver.find_element_by_xpath("// button[@ class ='dropdown-item dropdown-signout']").click()
            self.driver.get("https://github.com/login")
        else:
            sourceDF["result"] = 'fail'
            self.driver.get("https://github.com/login")
            print(sourceDF)
            sourceDF.to_excel("DDT.xlsx")
            assert "GitHub1" in title, "failed"


        print(sourceDF)
        sourceDF.to_excel("DDT.xlsx")





        # self.driver.find_element_by_xpath("//a[@class='HeaderMenu-link no-underline mr-3']").click()
        # lstofLinks = self.driver.find_elements_by_tag_name("a")
        # for i in range(0,len(lstofLinks)):
        # print('List of links .. ')
        # print(lstofLinks[i].text)
        # self.driver.find_element_by_link_text("//a[@class='HeaderMenu-link no-underline mr-3']").click()
        # print("entered in the loop")


        #if title == 'GitHub':
        #SourceData['result'][i] = 'Pass'
        #else:
        #SourceData['result'][i] = 'Fail'
        #assert title in "GitHub" , 'Login Credenetials has worked successfully..'






