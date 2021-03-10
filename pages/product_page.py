from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def check_alert_success(self):
        book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text
        alert_text = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE).text
        assert book_name == alert_text

    def check_cart_price_is_equal_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(
            *ProductPageLocators.BASKET_COST).text
        assert product_price in cart_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it didn't"
