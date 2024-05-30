from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        # Initialize the BasePage with the WebDriver instance and a WebDriverWait with a timeout of 10 seconds
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        try:
            # Wait until the element specified by the locator is present on the page
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            # Handle the case when the element is not found within the specified timeout
            print(f"Element: {locator}. Error: {e}")
