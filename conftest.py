import pytest
from selenium import webdriver

# Will be executed only once per test session
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
