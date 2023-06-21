import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class Test_parametrize():

    message = ''

    links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('urls', links)
    def test_func(self, browser, urls):
        
        browser.get(urls)
        
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

        time.sleep(8)
        
        input_field = browser.find_element(By.CLASS_NAME, "ember-text-area")
        input_field.send_keys(str(math.log(int(time.time()))))

        time.sleep(5)

        submit_btn = browser.find_element(By.CLASS_NAME, "submit-submission")
        submit_btn.click()
        
        time.sleep(10)

        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")

        assert 'Correct!' in message.text

        if __name__ == "__main__":
            pytest.main()
