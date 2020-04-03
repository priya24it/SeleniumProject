import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    global driver
   # browser_name=request.config.getoption("browser_name")
    if "chrome" == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\kbharathi\\Desktop\\MDM\\WebApp\\chromedriver\\chromedriver.exe")
    elif "chrome" == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif "chrome" == "IE":
        print("IE driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()