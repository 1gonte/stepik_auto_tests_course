import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  # открываем сайт
  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # считываем элемент x и находим значение уравнения
  x_element = browser.find_element(By.ID, "treasure")
  x_value = x_element.get_attribute("valuex")
  y = calc(x_value)

  # вводим ответ поле 
  input1 = browser.find_element(By.ID, "answer")
  input1.send_keys(y)

  # отмечаем чек-бокс
  checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
  checkbox.click()

  # выбираем радиобатон
  radio = browser.find_element(By.ID, "robotsRule")
  radio.click()

  btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  btn.click()

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()
