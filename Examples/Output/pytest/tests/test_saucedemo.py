# tests/test_saucedemo.py

import pytest

def test_saucedemo(login_page, inventory_page, cart_page, checkout_page, checkout_complete_page):
    login_page.navigate_to_login()
    login_page.input_username('standard_user')
    login_page.input_password('secret_sauce')
    login_page.click_login_button()

    inventory_page.click_item_link()
    inventory_page.click_add_to_cart_button()

    cart_page.click_shopping_cart_link()
    cart_page.click_checkout_button()

    checkout_page.input_first_name('Tom')
    checkout_page.input_last_name('Smith')
    checkout_page.input_postal_code('95052')
    checkout_page.click_continue_button()

    checkout_complete_page.click_finish_button()
