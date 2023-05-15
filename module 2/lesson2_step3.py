from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    num1 = num1.text
    num2 = num2.text
    num = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(num) # ищем элемент с суммой данных чисел

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта 
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
