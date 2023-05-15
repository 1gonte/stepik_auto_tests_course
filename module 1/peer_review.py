from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
# Ваш код, который заполняет обязательные поля
input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
input1.send_keys("Обязательно")
input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
input2.send_keys("Обязательно")
input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
input3.send_keys("Обязательно")
# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
time.sleep(1)
    # находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()
