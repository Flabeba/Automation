from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.TAG_NAME, 'input').send_keys("standard_user")
driver.find_element(By.NAME, 'password').send_keys("secret_sauce")
driver.find_element(By.ID, 'login-button').click()

sleep(3)

driver.quit()