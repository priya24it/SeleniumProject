import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.GoogleHomePage import HomePage
from PageObjects.GoogleSearchPage import SearchPage
from UtilityClass.utilityclass import commonclass
from keyboard import press
import keyboard

@pytest.mark.skip
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("passdata")
class Test_SampleGmail(commonclass):

    def test_scenarioforgoogleaccount(self):
        homePage = HomePage(self.driver)
        homePage.SendKeys()
        searchPage = SearchPage(self.driver)
        signinPage = searchPage.ClickonSigninLink()

        createaccount = signinPage.Clickoncreateaccountlink()
        assertapage = createaccount.createaccountwithtestdata()
        h1value = assertapage.Clickonassertpage()
        assert "Verifying your phone number" in h1value, "Both are matching"

        #keyboard.press_and_release('enter')




