from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, faker):
        self.login_page = LoginPage(browser, LoginPage.url)
        self.login_page.open()
        email = faker.unique.email()
        password = "MyStrongPassword123!"
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPage.url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPage.url)
        page.open()
        page.add_product_to_basket()
        page.should_be_product_added_message()
        page.should_be_basket_price_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPage.url)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPage.url)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProductPage.url)
    page.open()
    page.go_to_login_page()

@pytest.mark.parametrize('link', [f"{ProductPage.url_promo}{i}" for i in range(10)])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем драйвер и URL
    page.open()                          # открываем страницу товара
    page.add_product_to_basket()         # нажимаем кнопку добавления
    page.solve_quiz_and_get_code()       # решаем математическую проверку в alert

    # проверки после добавления
    page.should_be_product_added_message()  # проверяем, что название товара в сообщении совпадает
    page.should_be_basket_price_message()   # проверяем, что стоимость корзины совпадает с ценой товара