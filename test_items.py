from selenium.webdriver.common.by import By
import time

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def is_button_present(browser):
    try:
        browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
        return True
    except:
        return False

def test_exist_add_product_to_basket_button(browser):
    browser.get(LINK)
    # time.sleep(30)

    assert is_button_present(browser), 'Кнопка добавления товара в корзину не найдена'