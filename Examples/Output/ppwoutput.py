from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to URL
    page.goto('https://www.saucedemo.com/v1/')

    # Input text for username
    page.fill("input[name='user-name']", 'standard_user')

    # Input text for password
    page.fill("input[type='password'][id='password'][name='password'][placeholder='Password']", 'secret_sauce')

    # Click login button
    page.click("input.btn_action[type='submit'][id='login-button']")

    # Click on item link
    page.click("a[href='./inventory-item.html?id=5'][id='item_5_title_link']")

    # Click add to cart button
    page.click("button.btn_primary.btn_inventory")

    # Click shopping cart link
    page.click("a.shopping_cart_link.fa-layers.fa-fw[href='./cart.html']")

    # Click checkout button
    page.click("a.btn_action.checkout_button[href='./checkout-step-one.html']")

    # Input first name
    page.fill("input.form_input[id='first-name'][type='text'][placeholder='First Name']", 'Tom')

    # Input last name
    page.fill("input.form_input[id='last-name'][type='text'][placeholder='Last Name']", 'Smith')

    # Input postal code
    page.fill("input.form_input[id='postal-code'][type='text'][placeholder='Zip/Postal Code']", '95052')

    # Click continue button
    page.click("input.btn_primary.cart_button[type='submit']")

    # Click finish button
    page.click("a.btn_action.cart_button[href='./checkout-complete.html']")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
