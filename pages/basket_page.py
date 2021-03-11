from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.basket_is_empty()
        self.is_present_basket_empty_msg()

    def basket_is_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_LIST), \
            "Basket is not empty but should be"

    def is_present_basket_empty_msg(self):
        element = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MSG)
        element_text = element.text
        assert 'Your basket is empty.' in element_text
