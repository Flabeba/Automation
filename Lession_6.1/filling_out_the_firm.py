from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

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

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

if len(inputs) == len(datas):
    for num in range(0, len(inputs)):
        driver.find_element(By.NAME, inputs[num]).send_keys(datas[num])
    driver.find_element(By.TAG_NAME, 'button').click()

success_len = driver.find_elements(By.CSS_SELECTOR, 'div.alert-success')
if len(success_len) == len(inputs):
    print("Заполнено", len(success_len), "полей")

if driver.find_element(By.CSS_SELECTOR, '#zip-code.alert-danger'):
    print("Zip-code не заполнен")

driver.quit()