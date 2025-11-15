from .pages.product_page import ProductPage
import pytest

@pytest.mark.xfail(reason="Сообщение об успехе появляется, тест ожидает отсутствие")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.url)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPage.url)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Сообщение об успехе появляется, тест ожидает отсутствие")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.url)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_disappeared()

