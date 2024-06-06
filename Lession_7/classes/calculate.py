from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculate:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def waiting_time(self, driver, var_value):
        driver.find_element(By.ID, 'delay').clear()
        driver.find_element(By.ID, 'delay').send_keys(var_value[4])

    def waiting(self, driver, var_value):
        waiter = WebDriverWait(driver, int(var_value[4]) + 1)
        waiter.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'" + var_value[5] + "')]"))
        )

    def calc(self, driver, var_value):
        for clicker_keys in range(0, len(var_value) - 2):
            driver.find_element(By.XPATH, "//span[contains(text(),'" + var_value[clicker_keys] + "')]").click()

    def close(self, driver):
        driver.quit()