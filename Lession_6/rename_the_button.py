from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.TAG_NAME, 'input').send_keys("SkyPro")
driver.find_element(By.CLASS_NAME, 'btn-primary').click()
text_button = driver.find_element(By.CLASS_NAME, 'btn-primary').text
print("Текст на кнопке: " +text_button)

driver.quit()