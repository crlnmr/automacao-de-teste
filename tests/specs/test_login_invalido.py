from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from guara.application import Application
from guara import it
from tests.transactions.login_transaction import LoginWith
from tests.fixtures.driver import driver


def test_login_credenciais_invalidas(driver):

    # =========================
    # 1. LOGIN INVALIDO

    # =========================

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_invalida")
    driver.find_element(By.ID, "login-button").click()

    # Validacao mensagem de erro

    assert (
        "Username and password do not match"
        in driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    )


def test_login_invalido(driver):

    app = Application(driver)

    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="wrong_password",
    ).then(
        it.Contains,
        "Epic sadface: Username and password do not match any user in this service"
    )

