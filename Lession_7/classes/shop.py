from selenium.webdriver.common.by import By

class Shop:

    total_sum = ""

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def enpity(self, driver, id_on_page):
        driver.find_element(By.ID, id_on_page[0]).send_keys("standard_user") #Заполняем поле user
        driver.find_element(By.ID, id_on_page[1]).send_keys("secret_sauce")  #Заполняем поле password
        driver.find_element(By.ID, id_on_page[len(id_on_page) - 4]).click()

    def addition(self, driver, id_on_page):
        #Clicker_to_button
        for click_to_button in range(len(id_on_page) - 3, len(id_on_page)):
            driver.find_element(By.ID, id_on_page[click_to_button]).click()
    
    def basket(self, driver):
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()    #Переходим в корзину
    
    def data_to_customer(self, driver, form_delivery, datas):
        driver.find_element(By.NAME, 'checkout').click()
        for cycle_for_form in range(0, len(form_delivery) - 1):
            driver.find_element(By.NAME, form_delivery[cycle_for_form]).send_keys(datas[cycle_for_form])
        driver.find_element(By.NAME, form_delivery[3]).click()
    
    def total_sum(self, driver) -> total_sum:
        total_sum = driver.find_element(By.CLASS_NAME, 'summary_total_label').text

        if total_sum == "Total: $58.29":
            print(total_sum)
        else:
            print("Неверная сумма полного заказа")

    def close(self, driver):
        driver.quit()