import pytest
from selenium import webdriver
import psycopg2


# Fixture for setting up the Selenium WebDriver session
@pytest.fixture(scope="session", autouse=True)
def app(request):
    driver = webdriver.Chrome()
    # Set the window size to 1920x1080 pixels
    driver.set_window_size(1920, 1080)

    # Make the driver available to the request
    request.session.driver = driver
    yield driver
    driver.quit()


# Fixture for establishing a database connection
@pytest.fixture(scope="session")
def db_connection():
    # Database configuration details
    db_config = {
        'dbname': 'db_name',
        'user': 'db_user',
        'password': 'db_password',
        'host': 'localhost',
        'port': 5432
    }

    connection = psycopg2.connect(
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port']
    )
    yield connection
    connection.close()
