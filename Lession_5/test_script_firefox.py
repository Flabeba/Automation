from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#1 кейс: Клик по кнопке
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()

for click_in_button in range(1, 6):
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    sleep(1)

len_elements = driver.find_elements(By.CLASS_NAME, "added-manually") #Считаем количество кнопок Delete
print("Количество кнопок Delete в браузере Firefox:", len(len_elements)) #Выводим количество кнопок Delete

driver.quit() #Закрываем браузер


#2 кейс: Клик по кнопке без ID
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()

for element_not_id in range(1, 4):
    driver.find_element(By.CLASS_NAME, 'btn').click()

print("Нажали на кнопку без ID в Firefox")

driver.quit()


#3 rейс: Клик по кнопке с CSS-классом
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")
driver.maximize_window()

for click_in_button in range(1, 4):
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    sleep(2)
    driver.switch_to.alert.accept()
    sleep(3)

driver.quit()


#4 rейс: Модальное окно
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/entry_ad')
driver.maximize_window()

sleep(2)
driver.find_element(By.XPATH, '//p[contains(text(), "Close")]').click()
sleep(2)

driver.quit()


#5 кейс: Поле ввода
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/inputs')
driver.maximize_window()

driver.find_element(By.TAG_NAME, 'input').send_keys("1000")
sleep(3)

driver.find_element(By.TAG_NAME, 'input').clear()
sleep(2)

driver.find_element(By.TAG_NAME, 'input').send_keys("999")
sleep(2)

driver.quit()


#6 rейс: Форма авторизации
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

driver.find_element(By.NAME, 'username').send_keys("tomsmith")
driver.find_element(By.NAME, 'password').send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH, '//i[contains(text(), "Login")]').click()
sleep(3)

driver.quit()