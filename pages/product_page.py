from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_product_added_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == message_name, \
            f"Expected product name '{product_name}' but got '{message_name}' in success message."

    def should_be_basket_price_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_PRICE).text
        assert product_price == basket_price, \
            f"Expected basket price '{product_price}' but got '{basket_price}'."
