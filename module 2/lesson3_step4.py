import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  # открываем сайт
  link = "http://suninjuly.github.io/alert_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # нажимаем на кнопку
  button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  button.click()

  # переключаемся на модальное окно и принимаем его
  confirm = browser.switch_to.alert
  confirm.accept()
  
  # считываем элемент x и находим значение уравнения
  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  y = calc(x)

  # вводим ответ поле 
  input1 = browser.find_element(By.ID, "answer")
  input1.send_keys(y)

  btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  btn.click()

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()
  