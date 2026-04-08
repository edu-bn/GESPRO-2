from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import os

BASE_DIR = os.path.dirname(__file__)
ruta_archivo = os.path.join(BASE_DIR, "archivos", "plantilla.xlsx")
ruta_archivo = os.path.abspath(ruta_archivo)

def crear_proyecto(driver, nombre, archivo):
    """
    Ingresar a la pagina
    Presionar "Crear Proyecto"
    Ingresar nombre del proyecto
    Subir el archivo excel "plantilla.xlsx" descargado en el paso 3
    Presionar "+ Crear Proyecto"
    Presionar "Confirmar"
    Ingresar al proyecto recién creado
    """
     # Ver en qué URL estamos
    print(f"URL inicial: {driver.current_url}")
    time.sleep(2)
    
    #Presionar "Crear Proyecto"
    driver.find_element(By.ID, "crear_proyecto").click()
    time.sleep(1)
    print(f"URL inicial: {driver.current_url}")

    #Ingresar nombre del proyecto
    driver.find_element(By.NAME, "nombre_proyecto").send_keys(nombre)
    time.sleep(1)

    #Subir el archivo excel "plantilla.xlsx" descargado en el paso 3
    driver.find_element(By.NAME, "archivo").send_keys(archivo)
    time.sleep(1)

    #Presionar "+ Crear Proyecto"
    driver.find_element(By.NAME, "crear_proyecto").click()
    time.sleep(2)

    #Presionar "Confirmar"
    driver.find_element(By.ID, "btn-confirmar").click()
    time.sleep(2)

    #Ingresar al proyecto recién creado
    driver.find_element(By.ID, "Proyecto de prueba").click()
    time.sleep(2)

    driver.quit()   

def modificar_proyecto(driver, nombre):
    """
    Ingresar a la pagina
    Ingresar al proyecto creado en el caso 1
    Seleccionar "Lista" de la navbar
    Presionar el icono de lápiz al lado derecho de una actividad
    Modificar el texto en el input nombre situado primero
    Presionar "Guardar"
    """
    # Ver en qué URL estamos
    print(f"URL inicial: {driver.current_url}")
    time.sleep(2)

    #Ingresar al proyecto creado en el caso 1
    driver.find_element(By.ID, nombre).click()
    time.sleep(2)

    #Seleccionar "Lista" de la navbar
    driver.find_element(By.ID, "nav-lista").click()
    time.sleep(2)   

    #Presionar el icono de lápiz al lado derecho de una actividad
    driver.find_element(By.CLASS_NAME, "btn-editar").click()
    time.sleep(2)

    #Modificar el texto en el input nombre situado primero
    driver.find_element(By.ID, "editNombreInput").clear().send_keys("Actividad modwewficada")
    time.sleep(1)   

    #Presionar "Guardar"
    driver.find_element(By.ID, "saveChanges").click()
    time.sleep(2)

    driver.quit()

@pytest.mark.parametrize("nombre, ruta_archivo", [("Proyecto A", ruta_archivo), ("Proyecto B", ruta_archivo)])
def test_crear_proyecto(driver, nombre, ruta_archivo):
    crear_proyecto(driver, nombre, ruta_archivo)
    assert nombre in driver.page_source

@pytest.mark.parametrize("nombre", [("Proyecto A"), ("Proyecto B")])
def test_modificar_proyecto(driver, nombre):
    modificar_proyecto(driver, nombre)
    assert "Actividad modificada" in driver.page_source
