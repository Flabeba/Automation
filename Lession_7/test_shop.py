from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from classes.shop import Shop

id_on_page = ['user-name', 'password', 'login-button',
              'add-to-cart-sauce-labs-backpack', 'add-to-cart-sauce-labs-bolt-t-shirt',
              'add-to-cart-sauce-labs-onesie']

form_delivery = ['firstName', 'lastName', 'postalCode', 'continue']
datas = ['Мия', 'Мазаева', '105523']

<<<<<<< HEAD

def test_shop(id_on_page, form_delivery):
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    shop = Shop(driver)
    shop.get("https://www.saucedemo.com/") #Переходим на сайт
    shop.enpity(driver, id_on_page) #Заходим под пользователем
    shop.addition(driver, id_on_page) 
    shop.basket(driver)
    shop.data_to_customer(driver, form_delivery, datas)
    shop.total_sum(driver)
    shop.close(driver)

test_shop(id_on_page, form_delivery)
=======
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
shop = Shop(driver)
shop.get("https://www.saucedemo.com/") #Переходим на сайт
shop.enpity(driver, id_on_page) #Заходим под пользователем
shop.addition(driver, id_on_page) 
shop.basket(driver)
shop.data_to_customer(driver, form_delivery, datas)
shop.total_sum(driver)
shop.close(driver)
>>>>>>> refs/remotes/origin/lesson7
