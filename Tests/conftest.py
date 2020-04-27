import pytest
import pandas as pd
from selenium import webdriver
#from Testdata import TestDataLogin1
from UtilityClass.utilityclass import commonclass


driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="chromedriver\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    #driver.get("https://www.google.com")
    #driver.get("https://www.google.com")
    #driver.get("https://www.worldometers.info/geography/flags-of-the-world")
    #driver.get("https://www.guru99.com/handling-dynamic-selenium-webdriver.html")
    driver.get("http://demo.guru99.com/test/web-table-element.php")
    request.cls.driver = driver
    yield
    driver.close()

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

@pytest.fixture(params=[('priya', 'bharathi', 'karnati'), ('Ashok', 'Kumar', 'Samala')])
def passdatamultiplevalues123(request):
    return request.param

#@pytest.fixture(params=[dict])
dict = commonclass.testData("abc")
@pytest.fixture(params=[{"username":"Priya24it","password":"Abord@24"},{"username":"Priya24it34","password":"Abord@24"}])
def passexceldata(request):
    return request.param






