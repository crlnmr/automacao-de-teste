from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver


def test_remover_item_do_carrinho(driver):

    # =========================
    # 1. LOGIN
    # =========================

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # =========================
    # 2. ADICIONAR PRODUTO
    # =========================

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # =========================
    # 3. REMOVER PRODUTO
    # =========================

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Validacao carrinho vazio
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
