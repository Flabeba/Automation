from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from classes.filling_out_the_form import *

inputs = [
    'first-name', 'last-name', 'address', 
    'e-mail', 'phone', 'city', 'country', 
    'job-position', 'company'
]

datas = [
    "Иван", "Петров", "Ленина, 55-3",
    "test@skypro.com", "+7985899998787",
    "Москва", "Россия", "QA", "SkyPro"
]

def test_filling_out_the_form(inputs, datas):
    
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    form_ = Fields(driver)
    form_.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    form_.field(inputs, datas)
    form_.checking_field(inputs)
    form_.close(driver)

test_filling_out_the_form(inputs, datas)