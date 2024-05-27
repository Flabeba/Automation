from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from classes.calculate import Calculate

var_value = ["7", "+", "8", "=", "45", "15"]

def test_calculate(var_value):

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    waiting_calc = Calculate(driver)
    waiting_calc.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    waiting_calc.waiting_time(driver, var_value)
    waiting_calc.calc(driver, var_value)
    waiting_calc.waiting(driver, var_value)
    waiting_calc.close(driver)

test_calculate(var_value)
