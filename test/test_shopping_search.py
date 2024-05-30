from pages.home_page import HomePage
from pages.results_search_page import SearchResultsPage
from conftest import app


# Test method to verify successful search
def test_successful_search(app):
    driver = app
    home_page = HomePage(driver)
    home_page.search_item('iPhone 15')
    search_results_page = SearchResultsPage(driver)
    # Check if search results are displayed
    assert search_results_page.search_results_displayed(), 'Results were not displayed'


# Test method to verify unsuccessful search
def test_unsuccessful_search(app):
    driver = app
    home_page = HomePage(driver)
    home_page.search_item('hJndkjd1')
    search_results_page = SearchResultsPage(driver)
    # Check if the no results message is displayed
    assert search_results_page.search_no_results_displayed(), 'No results message was not displayed'
