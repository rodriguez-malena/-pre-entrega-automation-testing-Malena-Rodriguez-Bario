from selenium import webdriver
from selenium.webdriver.common.by import By

from auxiliar import login


def test_login_exitoso():

    driver = webdriver.Chrome()

    login(driver)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()


def test_navegacion_inventario():

    driver = webdriver.Chrome()

    login(driver)

    assert driver.title == "Swag Labs"

    titulo = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]')

    assert titulo.text == "Products"

    productos = driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')

    assert len(productos) > 0
    assert productos[0].is_displayed()

    driver.quit()

def test_elementos_interfaz():
    driver = webdriver.Chrome()
    
    login(driver)

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()
    
    filtro = driver.find_element(By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    assert filtro.is_displayed()
    
    carrito = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    assert carrito.is_displayed()

    driver.quit()


def test_agregar_productos():
    driver = webdriver.Chrome()
    
    login(driver)

    boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton_agregar.click()

    contador_carrito = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    assert contador_carrito.text == "1"

    carrito = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    carrito.click()

    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    producto = driver.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]')

    assert producto.text == "Sauce Labs Backpack"

    driver.quit()

