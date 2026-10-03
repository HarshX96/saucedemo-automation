import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage, CartPage
from data import USERS, PRODUCT_IDS, MENU_LINKS


def _login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(3)


# --- Test 1 ---
@pytest.mark.parametrize("link_id", list(MENU_LINKS.keys()))
@pytest.mark.parametrize("username", USERS)
def test_menu_shows_links(driver, username, link_id):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(2)
    assert inventory.get_menu_link_text(link_id) == MENU_LINKS[link_id]


# --- Test 2 ---
@pytest.mark.parametrize("username", USERS)
def test_x_button_closes_menu(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.close_burger_menu()
    time.sleep(1)
    assert inventory.get_menu_aria_hidden() == "true"


# --- Test 3 ---
@pytest.mark.smoke
@pytest.mark.parametrize("username", USERS)
def test_logout_returns_to_login(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.click_logout()
    time.sleep(1)
    assert "inventory" not in driver.current_url
    assert "https://www.saucedemo.com/" in driver.current_url


# --- Test 4 ---
@pytest.mark.parametrize("username", USERS)
def test_all_items_from_cart(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.click_all_items()
    time.sleep(1)
    assert "inventory.html" in driver.current_url


# --- Test 5 ---
@pytest.mark.parametrize("username", USERS)
def test_all_items_from_product_detail(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.click_all_items()
    time.sleep(1)
    assert "inventory.html" in driver.current_url


# --- Test 6 ---
@pytest.mark.parametrize("username", USERS)
def test_all_items_from_checkout_step_one(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(2)
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.click_all_items()
    time.sleep(1)
    assert "inventory.html" in driver.current_url


# --- Test 7 ---
@pytest.mark.parametrize("username", USERS)
def test_about_link_href(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(2)
    assert "saucelabs.com" in inventory.get_about_href()


# --- Test 8 ---
@pytest.mark.parametrize("username", USERS)
def test_about_click_opens_sauce_labs(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.click_about()
    time.sleep(2)
    assert "saucelabs.com" in driver.current_url
