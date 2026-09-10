from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver


def test_usuario_bloqueado(driver):

    # =========================
    # 1. USUARIO BLOQUEADO
    # =========================

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validacao mensagem de usuario bloqueado

    assert (
        "Sorry, this user has been locked out."
        in driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    )
