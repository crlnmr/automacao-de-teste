from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tests.fixtures.driver import driver


def teste_ordenacao_produtos_preco(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_visible_text(
        "Price (low to high)"
    )

    precos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    lista_precos = [float(preco.text.replace("$", "")) for preco in precos]
    assert lista_precos == sorted(lista_precos)
