from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        # Используем метод is_disappeared (с таймаутом по умолчанию SHORT_TIMEOUT)
        assert self.is_disappeared(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        # Используем метод find_element_with_wait с таймаутом DEFAULT_TIMEOUT
        assert self.find_element_with_wait(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"

