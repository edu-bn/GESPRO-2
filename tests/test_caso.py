from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "http://localhost:8000"

def test_pagina_carga():
    driver = webdriver.Chrome()
    
    driver.get(BASE_URL)

    # Validar que cargó la página
    print(f"Título real: '{driver.title}'")  # Ver qué título tiene
    assert "GESPRO" in driver.title

    driver.quit()


def caso1():
    """ ngresar a la pagina
    Presionar "Crear Proyecto"
    Presionar "Descargar plantilla Gantt"
    Ingresar nombre del proyecto
    Subir el archivo excel "plantilla.xlsx" descargado en el paso 3
    Presionar "+ Crear Proyecto"
    Confirmar datos
    Presionar "Confirmar"
    Ingresar al proyecto recién creado"""
    #Ingresar a la pagina
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    
    # Ver en qué URL estamos
    print(f"URL inicial: {driver.current_url}")
    time.sleep(2)
    
    #Presionar "Crear Proyecto"
    boton = driver.find_element(By.ID, "crear_proyecto")
    boton.click()
    time.sleep(1)
    print(f"URL inicial: {driver.current_url}")

    #Presionar "Descargar plantilla Gantt"

    #Ingresar nombre del proyecto
    input_nombre = driver.find_element(By.NAME, "nombre_proyecto")
    input_nombre.send_keys("Proyecto de prueba")
    time.sleep(1)

    #Subir el archivo excel "plantilla.xlsx" descargado en el paso 3
    input_file = driver.find_element(By.NAME, "archivo")
    input_file.send_keys("/home/Isaias/Repositorios/GESPRO-2/tests/archivos/plantilla.xlsx")
    time.sleep(1)

    #Presionar "+ Crear Proyecto"
    boton_crear = driver.find_element(By.NAME, "crear_proyecto")
    print(f"Botón encontrado: {boton_crear is not None}")
    boton_crear.click()
    time.sleep(2)

    #Presionar "Confirmar"
    boton_confirmar = driver.find_element(By.ID, "btn-confirmar")
    boton_confirmar.click()
    time.sleep(2)

    #Ingresar al proyecto recién creado
    proyecto_link = driver.find_element(By.ID, "Proyecto de prueba")
    proyecto_link.click()
    time.sleep(2)



    
    driver.quit()




def caso2():
    """
    Ingresar a la pagina
    Ingresar al proyecto creado en el caso 1
    Seleccionar "Lista" de la navbar
    Presionar el icono de lápiz al lado derecho de una actividad
    Modificar el texto en el input nombre situado primero
    Presionar "Guardar"
    """
     #Ingresar a la pagina
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    
    # Ver en qué URL estamos
    print(f"URL inicial: {driver.current_url}")
    time.sleep(2)

    #Ingresar al proyecto creado en el caso 1
    proyecto_link = driver.find_element(By.ID, "Proyecto de prueba")
    proyecto_link.click()
    time.sleep(2)

    #Seleccionar "Lista" de la navbar
    lista_link = driver.find_element(By.ID, "nav-lista")
    lista_link.click()
    time.sleep(2)   

    #Presionar el icono de lápiz al lado derecho de una actividad
    boton_editar = driver.find_element(By.ID, "btn-edit-93")
    boton_editar.click()
    time.sleep(2)

    #Modificar el texto en el input nombre situado primero
    input_nombre = driver.find_element(By.ID, "editNombreInput")
    input_nombre.clear()
    input_nombre.send_keys("Actividad modwewficada")
    time.sleep(1)   

    #Presionar "Guardar"
    boton_guardar = driver.find_element(By.ID, "saveChanges")
    boton_guardar.click()
    time.sleep(2)




    
    driver.quit()



if __name__ == "__main__":
    # caso1()
    caso2()
