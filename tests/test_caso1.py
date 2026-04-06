from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:8000"

def test_pagina_carga():
    driver = webdriver.Chrome()
    
    driver.get(BASE_URL)

    # Validar que cargó la página
    assert "Mi App" in driver.title

    driver.quit()


def test_input_y_click():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    # Buscar input y escribir
    input_box = driver.find_element(By.NAME, "q")
    input_box.send_keys("test")

    # Click en botón
    boton = driver.find_element(By.ID, "search-btn")
    boton.click()

    # Validar que pasó algo
    assert "resultados" in driver.page_source.lower()

    driver.quit()