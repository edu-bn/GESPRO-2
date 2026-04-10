from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
import os

BASE_DIR = os.path.dirname(__file__)
ruta_archivo = os.path.join(BASE_DIR, "archivos", "plantilla.xlsx")
ruta_archivo = os.path.abspath(ruta_archivo)
# ruta_archivo = "/home/Isaias/Repositorios/GESPROMM/tests/archivos/plantilla.xlsx"

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
    driver.find_element(By.ID, "crear_proyecto").click()
    time.sleep(2)

    #Presionar "Confirmar"
    driver.find_element(By.ID, "btn-confirmar").click()
    time.sleep(2)

    #Ingresar al proyecto recién creado
    driver.find_element(By.ID,nombre).click()
    time.sleep(2)



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
    time.sleep(1)

    #Seleccionar "Lista" de la navbar
    driver.find_element(By.ID, "nav-lista").click()
    time.sleep(1)   

    #Presionar el icono de lápiz al lado derecho de una actividad
    driver.find_element(By.CLASS_NAME, "btn-editar").click()
    time.sleep(1)

    #Modificar el texto en el input nombre situado primero
    driver.find_element(By.ID, "editNombreInput").clear()
    driver.find_element(By.ID, "editNombreInput").send_keys("Actividad modificada")
    time.sleep(1)   

    #Presionar "Guardar"
    driver.find_element(By.ID, "saveChanges").click()
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    time.sleep(2)


@pytest.mark.parametrize("setup_crear_proyecto", [("Proyecto A"), ("Proyecto B")], indirect=True)
def test_crear_proyecto(driver, setup_crear_proyecto):
    crear_proyecto(driver, setup_crear_proyecto, ruta_archivo)
    assert setup_crear_proyecto in driver.page_source
    driver.quit()   

@pytest.mark.parametrize("setup_modificar_proyecto", [("Proyecto A"), ("Proyecto B")], indirect=True)
def test_modificar_proyecto(driver, setup_modificar_proyecto):
    modificar_proyecto(driver, setup_modificar_proyecto)
    assert setup_modificar_proyecto in driver.page_source
    driver.quit()   
