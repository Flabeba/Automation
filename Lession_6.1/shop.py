from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

id_on_page = ['user-name', 'password', 'login-button',
              'add-to-cart-sauce-labs-backpack', 'add-to-cart-sauce-labs-bolt-t-shirt',
              'add-to-cart-sauce-labs-onesie']  #СОздаём список ID в магазине

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) #Открываем Firefox
driver.maximize_window() #разворачиваем окно браузера в максимальный размер

driver.get("https://www.saucedemo.com/") #Переходим на сайт

driver.find_element(By.ID, id_on_page[0]).send_keys("standard_user") #Заполняем поле user
driver.find_element(By.ID, id_on_page[1]).send_keys("secret_sauce")  #Заполняем поле password

one_click_button = len(id_on_page) - 4  #Вычисляем номер элемента кнопки 'Login' в списке id_on_page

#Clicker_to_button
for click_to_button in range(one_click_button, len(id_on_page)):
    driver.find_element(By.ID, id_on_page[click_to_button]).click()     #Цикл для обработки входа на сайт и добавления товаров

driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()    #Переходим в корзину
driver.find_element(By.NAME, 'checkout').click()

form_delivery = ['firstName', 'lastName', 'postalCode', 'continue']
datas = ['Мия', 'Мазаева', '105523']

for cycle_for_form in range(0, len(form_delivery) - 1):
        driver.find_element(By.NAME, form_delivery[cycle_for_form]).send_keys(datas[cycle_for_form])
driver.find_element(By.NAME, form_delivery[3]).click()

total_sum = driver.find_element(By.CLASS_NAME, 'summary_total_label').text

driver.quit()

if total_sum == "Total: $58.29":
    print(total_sum)
else:
     print("Неверная сумма полного заказа")