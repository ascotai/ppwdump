# pages/checkout_page.py

from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = "input.form_input[id='first-name'][type='text'][placeholder='First Name']"
        self.last_name_input = "input.form_input[id='last-name'][type='text'][placeholder='Last Name']"
        self.postal_code_input = "input.form_input[id='postal-code'][type='text'][placeholder='Zip/Postal Code']"
        self.continue_button = "input.btn_primary.cart_button[type='submit']"

    def input_first_name(self, first_name: str):
        self.page.fill(self.first_name_input, first_name)

    def input_last_name(self, last_name: str):
        self.page.fill(self.last_name_input, last_name)

    def input_postal_code(self, postal_code: str):
        self.page.fill(self.postal_code_input, postal_code)

    def click_continue_button(self):
        self.page.click(self.continue_button)
