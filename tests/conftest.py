import pytest
import requests
from selenium import webdriver
import os 
import django
import sys

BASE_URL = "http://localhost:8000"
BASE_DIR = os.path.dirname(__file__)
BACKEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "../backend"))

sys.path.append(BACKEND_DIR)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


def eliminar_proyecto(nombre):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gespro.settings')
    django.setup()
    from proyectos.models import Proyecto
    Proyecto.objects.filter(nombre=nombre).delete()


@pytest.fixture
def setup_crear_proyecto(request):
    #Setup
    nombre = request.param
    
    yield nombre

    #Teardown
    eliminar_proyecto(nombre)


@pytest.fixture
def setup_modificar_proyecto(driver, request):
    #Setup
    nombre = request.param
    ruta_archivo = os.path.abspath(os.path.join(BASE_DIR, "archivos", "plantilla.xlsx"))

    requests.post("http://localhost:8000/excel/importar_proyecto/", data={'nombre_proyecto': nombre, 'archivo': ruta_archivo})
    
    driver.refresh()

    yield nombre

    #Teardown
    eliminar_proyecto(nombre)
