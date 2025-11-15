from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage():
    DEFAULT_TIMEOUT = 10
    SHORT_TIMEOUT = 4
    ALERT_TIMEOUT = 5

    base_url = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser, url, timeout=DEFAULT_TIMEOUT):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def find_element_with_wait(self, how, what, timeout=None):
        wait_time = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.browser, wait_time).until(
            EC.presence_of_element_located((how, what))
        )

    def click_element(self, how, what, timeout=None):
        element = self.find_element_with_wait(how, what, timeout)
        element.click()

    def get_element_text(self, how, what, timeout=None):
        element = self.find_element_with_wait(how, what, timeout)
        return element.text

    def is_disappeared(self, how, what, timeout=SHORT_TIMEOUT):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
            return True
        except TimeoutException:
            return False

    def go_to_basket_page(self):
        self.click_element(*BasePageLocators.BASKET_LINK)

    def go_to_login_page(self):
        self.click_element(*BasePageLocators.LOGIN_LINK)

    def should_be_login_link(self):
        assert self.find_element_with_wait(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.find_element_with_wait(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"




