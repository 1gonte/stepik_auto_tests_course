import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exist_add_to_cart_button(browser):
	# переход на нужную страницу
    browser.get(link)
	# поиск кнопки добавления товара в корзину
    WebDriverWait(browser, 3).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "No add to cart button on page")
    btn = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    
    btn.click()

    WebDriverWait(browser, 3).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "alertinner")), "No book added message")
    
    message = browser.find_element(By.CLASS_NAME, "alertinner")
    assert "Coders at Work" in message.text
    