# pages/item_page.py

from playwright.sync_api import Page

class ItemPage:
    def __init__(self, page: Page):
        self.page = page

    def click_add_to_cart_button(self):
        self.page.click("button.btn_primary.btn_inventory")
