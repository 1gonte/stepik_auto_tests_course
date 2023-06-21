import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://stepik.org/lesson/236895/step/1'

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_auth(browser):
    browser.get(link)
    time.sleep(5)
    button_1st_login = browser.find_element(By.ID, "ember33")
    button_1st_login.click()
    time.sleep(3)

    button_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='E-mail']")
    button_email.send_keys("email")

    button_passw = browser.find_element(By.CSS_SELECTOR, "[placeholder='Пароль']")
    button_passw.send_keys("password")

    button_2nd_login = browser.find_element(By.CLASS_NAME, "button_with-loader")
    button_2nd_login.click()

    time.sleep(5)


    