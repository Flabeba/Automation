from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

var_value = ["7", "+", "8", "=", "45", "15"]

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
waiter = WebDriverWait(driver, int(var_value[4]) + 1)

driver.find_element(By.ID, 'delay').clear()
driver.find_element(By.ID, 'delay').send_keys(var_value[4])

for clicker_keys in range(0, len(var_value) - 2):
    driver.find_element(By.XPATH, "//span[contains(text(),'" + var_value[clicker_keys] + "')]").click()

waiter.until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'" + var_value[5] + "')]"))
)

driver.quit()