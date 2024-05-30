from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


def db_check_item(db_connection):
    # Check if the item exists in the database
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT * FROM items WHERE name = %s", ('iPhone 15',))
        item = cursor.fetchone()
        return item is not None


class ItemDetailsPage(BasePage):

    def item_details_displayed(self):
        try:
            # Check if the item details section is displayed
            element = self.wait_for_element((By.CSS_SELECTOR, '.add-to-cart'))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")
            return False

    def add_to_cart(self):
        try:
            # Click on the "Add to Cart" button
            add_to_cart_button = self.wait_for_element((By.CSS_SELECTOR, '.add-to-cart'))
            add_to_cart_button.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")
