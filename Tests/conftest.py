import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    global driver
   # browser_name=request.config.getoption("browser_name")
    if "chrome" == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\kbharathi\\Desktop\\MDM\\WebApp\\chromedriver\\chromedriver.exe")
        #driver = webdriver.Chrome(executable_path="",chrome_options="",desired_capabilities="")
        driver.current_url
    elif "chrome" == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif "chrome" == "IE":
        print("IE driver")
    driver.get("https://www.google.com")
    driver.maximize_window()

    request.cls.driver = driver

@pytest.fixture
def passdata():
    x = ["Priya Bharathi","Ashok kumar samala","Alexder"]
    return  x
