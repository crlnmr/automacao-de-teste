from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def login(self, user, password):
        self.type(*self.USERNAME, user)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)

    def __init__(self, driver):
        self.driver = driver

    def fill_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
