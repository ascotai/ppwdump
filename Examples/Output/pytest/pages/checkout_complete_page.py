# pages/checkout_complete_page.py

from playwright.sync_api import Page

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = "a.btn_action.cart_button[href='./checkout-complete.html']"

    def click_finish_button(self):
        self.page.click(self.finish_button)

