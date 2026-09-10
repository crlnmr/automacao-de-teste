from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_foo():
    # Inicializa o ChromeDriver automaticamente
    driver = webdriver.Chrome()

    try:
        # 1. Abre a URL inicial
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        time.sleep(2)  # Pausa apenas para você visualizar a ação

        # tenta encontrar o elemento na tela
        driver.find_element(By.ID, "my-text-id").send_keys("foo")
        driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[2]/button").click()
        time.sleep(15)  # Pausa apenas para você visualizar a ação

    finally:
        # Fecha o navegador e encerra o processo
        driver.quit()
