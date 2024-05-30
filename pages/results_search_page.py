from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    def search_results_displayed(self):
        try:
            # Check if search results are displayed
            element = self.wait_for_element((By.CSS_SELECTOR, '.search-results-product'))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")
            return False

    def search_no_results_displayed(self):
        try:
            # Check if no search results message is displayed
            element = self.wait_for_element((By.CSS_SELECTOR, '.empty-search-results-product'))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")
            return False

    def click_on_item(self):
        try:
            # Click on the first item in the search results
            first_item = self.wait_for_element((By.CSS_SELECTOR, '.search-results-product .item'))
            first_item.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")
