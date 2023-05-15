import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  # открываем сайт
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # нажимаем на кнопку
  button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  button.click()

  # определяем новую вкладку и переходим на нее
  second_window = browser.window_handles[1]
  browser.switch_to.window(second_window)
  
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