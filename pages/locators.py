from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alert-success:nth-child(1) strong")
    SUCCESS_MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages div.alert-info:nth-child(3) strong")
    

    
    