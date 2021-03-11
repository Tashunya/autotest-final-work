import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city" \
           "-and-the-stars_95/ "
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city" \
           "-and-the-stars_95/ "
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders" \
           "-handbook_209/?promo=newYear "
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_alert_success()
    page.check_cart_price_is_equal_product_price()


offer_list = range(0, 10)


@pytest.mark.parametrize('promo', [*range(7),
                                   pytest.param(7, marks=pytest.mark.xfail),
                                   *range(8, 10)])
def test_guest_can_add_product_to_basket_offers(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           f'-work_207/?promo=offer{promo}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_alert_success()
    page.check_cart_price_is_equal_product_price()


@pytest.mark.xfail(reason='msg appears')
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           '-work_207/ '
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           '-work_207/ '
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='msg should be closed')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           '-work_207/ '
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           '-work_207/ '
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function')
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        login_page = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
               '-work_207/ '
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
               '-work_207/ '
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.check_alert_success()
        page.check_cart_price_is_equal_product_price()
