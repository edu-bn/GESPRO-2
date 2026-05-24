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
    
    #Presionar "Crear Proyecto"
    driver.find_element(By.ID, "crear_proyecto").click()
    print(f"URL inicial: {driver.current_url}")

    #Ingresar nombre del proyecto
    driver.find_element(By.NAME, "nombre_proyecto").send_keys(nombre)

    #Subir el archivo excel "plantilla.xlsx" descargado en el paso 3
    driver.find_element(By.NAME, "archivo").send_keys(archivo)

    #Presionar "+ Crear Proyecto"
    driver.find_element(By.ID, "crear_proyecto").click()

    #Presionar "Confirmar"
    driver.find_element(By.ID, "btn-confirmar").click()

    #Ingresar al proyecto recién creado
    driver.find_element(By.ID,nombre).click()



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

    #Ingresar al proyecto creado en el caso 1
    driver.find_element(By.ID, nombre).click()

    #Seleccionar "Lista" de la navbar
    driver.find_element(By.ID, "nav-lista").click()

    #Presionar el icono de lápiz al lado derecho de una actividad
    driver.find_element(By.CLASS_NAME, "btn-editar").click()
    

    #Modificar el texto en el input nombre situado primero
    driver.find_element(By.ID, "editNombreInput").clear()
    driver.find_element(By.ID, "editNombreInput").send_keys("Actividad modificada")
    

    #Presionar "Guardar"
    driver.find_element(By.ID, "saveChanges").click()
    
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    


@pytest.mark.parametrize("setup_crear_proyecto", [("Proyecto A"), ("Proyecto C")], indirect=True)
def test_crear_proyecto(driver, setup_crear_proyecto):
    crear_proyecto(driver, setup_crear_proyecto, ruta_archivo)
    assert setup_crear_proyecto in driver.page_source
    driver.quit()   

@pytest.mark.parametrize("setup_modificar_proyecto", [("Proyecto A"), ("Proyecto C")], indirect=True)
def test_modificar_proyecto(driver, setup_modificar_proyecto):
    modificar_proyecto(driver, setup_modificar_proyecto)
    assert setup_modificar_proyecto in driver.page_source
    driver.quit()   
