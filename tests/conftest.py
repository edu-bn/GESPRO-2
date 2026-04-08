import pytest
from selenium import webdriver

BASE_URL = "http://localhost:8000"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()