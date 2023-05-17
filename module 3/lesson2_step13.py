from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class test_test(unittest.TestCase):

    def test_registration1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля: First name, last name, email
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder=Input your first name]")
        input1.send_keys("Ilon")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder=Input your last name]")
        input2.send_keys("Mask")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder=Input your email]")
        input3.send_keys("spacex.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual_welcome_text = welcome_text_elt.text
        expected_welcome_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(expected_welcome_text, actual_welcome_text, "expected '{expected_welcome_text}', got '{actual_welcome_text}'")

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля: First name, last name, email
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder=Input your first name]")
        input1.send_keys("Ilon")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder=Input your last name]")
        input2.send_keys("Mask")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder=Input your email]")
        input3.send_keys("spacex.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        actual_welcome_text = welcome_text_elt.text
        expected_welcome_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(expected_welcome_text, actual_welcome_text, "expected '{expected_welcome_text}', got '{actual_welcome_text}'")

        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__": 
    unittest.main()