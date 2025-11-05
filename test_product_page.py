from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
])

def test_guest_can_add_product_to_basket(browser, link):

    page = ProductPage(browser, link)   # инициализируем Page Object, передаем драйвер и URL
    page.open()                          # открываем страницу товара
    page.add_product_to_basket()         # нажимаем кнопку добавления
    page.solve_quiz_and_get_code()       # решаем математическую проверку в alert

    # проверки после добавления
    page.should_be_product_added_message()  # проверяем, что название товара в сообщении совпадает
    page.should_be_basket_price_message()   # проверяем, что стоимость корзины совпадает с ценой товара
