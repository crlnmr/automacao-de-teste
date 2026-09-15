from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_container")

    def is_loaded(self):
        try:
            self.find(*self.INVENTORY_CONTAINER)
            return True
        except:
            return False

    def add_product(self):
        self.click(*self.ADD_BACKPACK)

    def go_to_cart(self):
        self.click(*self.CART)
