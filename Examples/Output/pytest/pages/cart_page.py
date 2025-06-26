# pages/cart_page.py

from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_link = "a.shopping_cart_link.fa-layers.fa-fw[href='./cart.html']"
        self.checkout_button = "a.btn_action.checkout_button[href='./checkout-step-one.html']"

    def click_shopping_cart_link(self):
        self.page.click(self.shopping_cart_link)

    def click_checkout_button(self):
        self.page.click(self.checkout_button)


