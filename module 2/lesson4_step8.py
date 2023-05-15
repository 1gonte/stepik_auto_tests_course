import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  # открываем сайт
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # ждем пока цена опустится до 100$ и жмем на кнопку Book
  button = browser.find_element(By.ID, "book")
  price_waiting = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
  button.click() 
  
  # считываем элемент x и находим значение уравнения
  browser.execute_script("window.scrollBy(0, 200);")
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
