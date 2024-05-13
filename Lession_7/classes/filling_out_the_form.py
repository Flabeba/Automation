from selenium.webdriver.common.by import By

class Fields:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def field(self, inputs, datas):
        if len(inputs) == len(datas):
            for num in range(0, len(inputs)):
                self.driver.find_element(By.NAME, inputs[num]).send_keys(datas[num])
            return self.driver.find_element(By.TAG_NAME, 'button').click()

    def checking_field(self, inputs):
        success_len = self.driver.find_elements(By.CSS_SELECTOR, 'div.alert-success')
        if len(success_len) == len(inputs):
            print("Заполнено", len(success_len), "полей")

        if self.driver.find_element(By.CSS_SELECTOR, '#zip-code.alert-danger'):
            print("Zip-code не заполнен")
    
    def close(self, driver):
        driver.quit()