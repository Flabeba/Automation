from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculate:

    def __init__(self, driver):
        """Метод открывает окно браузера"""
        self.driver = driver

    def get(self, url):
        """Метод принимает на вход url для перехода по адресу
        и разворачивает окно браузера в максимальный вид"""
        self.driver.maximize_window()
        self.driver.get(url)

    def waiting_time(self, driver, var_value):
        """Метод принимает на вход список var_valur, в котором
        элемент с индексом 4 указывает на время, устанавливаемое 
        для ожидания ответа от сервера"""
        driver.find_element(By.ID, 'delay').clear()
        driver.find_element(By.ID, 'delay').send_keys(var_value[4])

    def waiting(self, driver, var_value):
        """Метод принимает на вход список var_value, в котором 
        элемент с индексом 5 указывает на ожидаемый ответ от решения задачи"""
        waiter = WebDriverWait(driver, int(var_value[4]) + 1)
        waiter.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'" + var_value[5] + "')]"))
        )

    def calc(self, driver, var_value):
        """Метод принимает на вход список var_value, в котором
        элементы с 0 по 4 имеют значения кнопок, нажимаемых для решения задачи"""
        for clicker_keys in range(0, len(var_value) - 2):
            driver.find_element(By.XPATH, "//span[contains(text(),'" + var_value[clicker_keys] + "')]").click()

    def close(self, driver):
        """Метод закрывает браузер"""
        driver.quit()