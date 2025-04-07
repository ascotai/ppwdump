# pages/inventory_page.py

from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_link = "a[href='./inventory-item.html?id=5'][id='item_5_title_link']"
        self.add_to_cart_button = "button.btn_primary.btn_inventory"

    def click_item_link(self):
        self.page.click(self.item_link)

    def click_add_to_cart_button(self):
        self.page.click(self.add_to_cart_button)

