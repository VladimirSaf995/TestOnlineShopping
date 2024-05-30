from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        # Initialize the HomePage with the WebDriver instance and navigate to the home page URL
        super().__init__(driver)
        self.driver.get('https://onlineshoping.com')

    def search_item(self, item_name):
        try:
            # Locate the search field, clear it, enter the item name, and submit the search
            search_field = self.wait_for_element((By.NAME, 'search-items'))
            search_field.clear()
            search_field.send_keys(item_name)
            search_field.submit()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")

    def browse_items(self):
        try:
            # Locate the browse items button and click on it
            browse_button = self.wait_for_element((By.ID, 'browse-items-button'))
            browse_button.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")
