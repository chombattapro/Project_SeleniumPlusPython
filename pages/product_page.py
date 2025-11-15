from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math

class ProductPage(BasePage):

    url = f"{BasePage.base_url}/catalogue/the-city-and-the-stars_95/"
    url_promo = f"{BasePage.base_url}/catalogue/coders-at-work_207/?promo=offer"

    def add_product_to_basket(self):
        self.click_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def should_be_product_added_message(self):
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        message_name = self.get_element_text(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
        assert product_name == message_name, \
            f"Expected product name '{product_name}' but got '{message_name}' in success message."

    def should_be_basket_price_message(self):
        product_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.get_element_text(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_PRICE)
        assert product_price == basket_price, \
            f"Expected basket price '{product_price}' but got '{basket_price}'."

    def should_not_be_success_message(self):
        is_disappeared = self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
        assert is_disappeared, "Success message is presented, but should not be."

    def should_be_success_message_disappeared(self):
        disappeared = self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
        assert disappeared, "Success message did not disappear as expected."

    def solve_quiz_and_get_code(self):
        try:
            WebDriverWait(self.browser, self.ALERT_TIMEOUT * 2).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs(12 * math.sin(float(x)))))
            alert.send_keys(answer)
            alert.accept()
            try:
                WebDriverWait(self.browser, self.ALERT_TIMEOUT).until(EC.alert_is_present())
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except TimeoutException:
                print("No second alert presented")
        except TimeoutException:
            print("Alert did not appear within the timeout period")