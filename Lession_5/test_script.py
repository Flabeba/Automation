from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert

#1.1 Кейс: Клик по кнопке (Google Chrome)
gchrome = webdriver.Chrome()
gchrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
gchrome.fullscreen_window()

for click_in_button in range(1, 6):
    gchrome.find_element(By.CSS_SELECTOR, 'button').click()
    sleep(2)

len_elements = gchrome.find_elements(By.CLASS_NAME, "added-manually") #Считаем количество кнопок Delete
print("Количество кнопок Delete в браузере Google Chrome:", len(len_elements)) #Выводим количество кнопок Delete

gchrome.close() #Закрываем браузер

#1.2 Кейс: Клик по кнопке (Firefox)
firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")
firefox.fullscreen_window()

for click_in_button in range(1, 6):
    firefox.find_element(By.CSS_SELECTOR, 'button').click()
    sleep(1)

len_elements = firefox.find_elements(By.CLASS_NAME, "added-manually") #Считаем количество кнопок Delete
print("Количество кнопок Delete в браузере Firefox:", len(len_elements)) #Выводим количество кнопок Delete

firefox.close() #Закрываем браузер

#2.1 Кейс: Клик по кнопке без ID (Google Chrome)
gchrome = webdriver.Chrome()
gchrome.get("http://uitestingplayground.com/dynamicid")
gchrome.fullscreen_window()

for element_not_id in range(1, 4):
    gchrome.find_element(By.CLASS_NAME, 'btn').click()
    sleep(2)

print("Нажали на кнопку без ID в Google Chrome")

gchrome.close()

#2.2 Кейс: Клик по кнопке без ID (Firefox)
firefox = webdriver.Firefox()
firefox.get("http://uitestingplayground.com/dynamicid")
firefox.fullscreen_window()

for element_not_id in range(1, 4):
    firefox.find_element(By.CLASS_NAME, 'btn').click()

print("Нажали на кнопку без ID в Firefox")

firefox.close()

#3.1 Кейс: Клик по кнопке с CSS-классом (Google Chrome)
gchrome = webdriver.Chrome()
gchrome.get("http://uitestingplayground.com/classattr")
gchrome.fullscreen_window()

for click_in_button in range(1, 4):
    gchrome.find_element(By.CLASS_NAME, 'btn-primary').click()
    sleep(2)
    gchrome.switch_to.alert.accept()
    sleep(3)

gchrome.close()

#3.2 Кейс: Клик по кнопке с CSS-классом (Firefox)
firefox = webdriver.Firefox()
firefox.get("http://uitestingplayground.com/classattr")
firefox.fullscreen_window()

for click_in_button in range(1, 4):
    firefox.find_element(By.CLASS_NAME, 'btn-primary').click()
    sleep(2)
    firefox.switch_to.alert.accept()
    sleep(3)

firefox.close()

#4.1 Кейс: Модальное окно (Google Chrome)
gchrome = webdriver.Chrome()
gchrome.get('https://the-internet.herokuapp.com/entry_ad')
gchrome.fullscreen_window()

sleep(3)
gchrome.find_element(By.XPATH, '//p[contains(text(), "Close")]').click()
sleep(2)

gchrome.close()

#4.2 Кейс: Модальное окно (Firefox)
firefox = webdriver.Firefox()
firefox.get('https://the-internet.herokuapp.com/entry_ad')
firefox.fullscreen_window()

sleep(2)
firefox.find_element(By.XPATH, '//p[contains(text(), "Close")]').click()
sleep(2)

firefox.close()

#5.1 Кейс: Поле ввода (Google Chrome)
gchrome = webdriver.Chrome()
gchrome.get('https://the-internet.herokuapp.com/inputs')
gchrome.fullscreen_window()

gchrome.find_element(By.TAG_NAME, 'input').send_keys("1000")
sleep(3)

gchrome.find_element(By.TAG_NAME, 'input').clear()
sleep(2)

gchrome.find_element(By.TAG_NAME, 'input').send_keys("999")
sleep(2)

gchrome.close()

#5.2 Кейс: Поле ввода (Firefox)
firefox = webdriver.Firefox()
firefox.get('https://the-internet.herokuapp.com/inputs')
firefox.fullscreen_window()

firefox.find_element(By.TAG_NAME, 'input').send_keys("1000")
sleep(3)

firefox.find_element(By.TAG_NAME, 'input').clear()
sleep(2)

firefox.find_element(By.TAG_NAME, 'input').send_keys("999")
sleep(2)

firefox.close()

#6.1 Кейс: Форма авторизации (Google Chrome)
gchrome = webdriver.Chrome()
gchrome.get('https://the-internet.herokuapp.com/login')
gchrome.fullscreen_window()

gchrome.find_element(By.NAME, 'username').send_keys("tomsmith")
gchrome.find_element(By.NAME, 'password').send_keys("SuperSecretPassword!")
gchrome.find_element(By.XPATH, '//i[contains(text(), "Login")]').click()
sleep(3)

gchrome.close()

#6.2 Кейс: Форма авторизации (Firefox)
firefox = webdriver.Firefox()
firefox.get('https://the-internet.herokuapp.com/login')
firefox.fullscreen_window()

firefox.find_element(By.NAME, 'username').send_keys("tomsmith")
firefox.find_element(By.NAME, 'password').send_keys("SuperSecretPassword!")
firefox.find_element(By.XPATH, '//i[contains(text(), "Login")]').click()
sleep(3)

firefox.close()