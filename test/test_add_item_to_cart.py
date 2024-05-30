from pages.home_page import HomePage
from pages.results_search_page import SearchResultsPage
from pages.item_details_page import ItemDetailsPage, db_check_item
from pages.cart_page import CartPage
from conftest import app, db_connection


def test_add_item_to_cart(app, db_connection):
    driver = app
    home_page = HomePage(driver)
    home_page.search_item('iPhone 15')
    search_results_page = SearchResultsPage(driver)
    search_results_page.click_on_item()
    item_details_page = ItemDetailsPage(driver)
    item_details_page.add_to_cart()
    cart_page = CartPage(driver)
    # Check if the cart confirmation message is displayed
    assert cart_page.cart_confirmation_displayed(), 'Cart confirmation was not displayed'
    # Check if the item is added to the database
    assert db_check_item(db_connection), 'Item was not added to the database'
