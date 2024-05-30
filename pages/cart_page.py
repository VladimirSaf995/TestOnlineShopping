from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class CartPage(BasePage):

    def cart_confirmation_displayed(self):
        try:
            # Check if the cart confirmation message is displayed
            element = self.wait_for_element((By.CSS_SELECTOR, '.cart-confirmation-product'))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException) as e:
            # Handle the case when the element is not found or timeout occurs
            print(f"Error: {e}")
            return False

    def items_list_displayed(self):
        try:
            # Check if the items list is displayed
            element = self.wait_for_element((By.CSS_SELECTOR, '.items-list'))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException) as e:
            # Handle the case when the element is not found or timeout occurs
            print(f"Error: {e}")
            return False
