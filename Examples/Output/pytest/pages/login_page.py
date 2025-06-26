# pages/login_page.py

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input[name='user-name']"
        self.password_input = "input[type='password'][id='password'][name='password'][placeholder='Password']"
        self.login_button = "input.btn_action[type='submit'][id='login-button']"

    def navigate_to_login(self):
        self.page.goto('https://www.saucedemo.com/v1/')

    def input_username(self, username: str):
        self.page.fill(self.username_input, username)

    def input_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_login_button(self):
        self.page.click(self.login_button)
