from pages.home_page import HomePage
from pages.item_details_page import ItemDetailsPage
from pages.results_search_page import SearchResultsPage
from pages.cart_page import CartPage
from conftest import app


# Test method to verify browsing items
def test_browse_items(app):
    driver = app
    home_page = HomePage(driver)
    home_page.browse_items()
    cart_page = CartPage(driver)
    # Check if the items list is displayed on the cart page
    assert cart_page.items_list_displayed(), 'Items list was not displayed'


# Test method to verify viewing item details
def test_view_item_details(app):
    driver = app
    home_page = HomePage(driver)
    home_page.search_item('iPhone 15')
    search_results_page = SearchResultsPage(driver)
    search_results_page.click_on_item()
    item_details_page = ItemDetailsPage(driver)
    # Check if the item details are displayed on the item details page
    assert item_details_page.item_details_displayed(), 'Item details were not displayed'
