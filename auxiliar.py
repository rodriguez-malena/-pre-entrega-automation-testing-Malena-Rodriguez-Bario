from selenium.webdriver.common.by import By


def login(driver, usuario="standard_user", clave="secret_sauce"):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(clave)
    driver.find_element(By.ID, "login-button").click()
