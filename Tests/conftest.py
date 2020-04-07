import pytest
import pandas as pd
from selenium import webdriver

from UtilityClass.utilityclass import commonclass


@pytest.fixture(scope="class")
def setup(request):
    global driver
   # browser_name=request.config.getoption("browser_name")
    if "chrome" == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\kbharathi\\Desktop\\MDM\\WebApp\\chromedriver\\chromedriver.exe")
        #driver = webdriver.Chrome(executable_path="",chrome_options="",desired_capabilities="")
        #driver.find_element()
    elif "chrome" == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif "chrome" == "IE":
        print("IE driver")
    driver.get("https://www.google.com")
    driver.maximize_window()

    request.cls.driver = driver

@pytest.fixture
def passdata():
    x = ["Priya Bharathi","Ashok kumar samala","TimeosfIndal18India","DeccanChornical@12345","DeccanChornical@12345"]
    return  x

@pytest.fixture(params=["priya","bharathi","karnati"])
def passdictdata(request):
    return request.param


@pytest.fixture(params=[('priya','bharathi','karnati'),('Ashok','Kumar','Samala')])
def passdatamultiplevalues(request):
    return request.param

#testdata = ""
#@pytest.fixture(params=[("TimeosfIndal", "TimeosfIndal", "TimeosfIndal18India", "DeccanChornical@12345", "DeccanChornical@12345"), ("DeccanChorinical ", "DeccanChorinical ", "DeccanChorinical18India", "DeccanChornical@12345", "DeccanChornical@12345")])
#testdata = commonclass.getTestdatatocreateaccount()
#@pytest.fixture(params=testdata)
#def passdatafromexcel(request):
   # return request.param


