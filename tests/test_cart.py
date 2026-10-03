import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage, CartPage
from data import USERS, PRODUCT_IDS, PRODUCT_DATA, LABELS


def _login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(3)


# --- Test 1 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_item_name(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(product)
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_item_name() == PRODUCT_DATA[product]["name"]


# --- Test 2 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_item_price(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(product)
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_item_price() == PRODUCT_DATA[product]["price"]


# --- Test 3 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_item_description(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(product)
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_item_description() == PRODUCT_DATA[product]["description"]


# --- Test 4 ---
@pytest.mark.parametrize("username", USERS)
def test_quantity_shows_one(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_quantity() == "1"


# --- Test 5 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_remove_on_cart_page_empties_cart(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(product)
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.remove_item(product)
    time.sleep(1)
    assert cart.is_cart_empty()


# --- Test 6 ---
@pytest.mark.parametrize("username", USERS)
def test_continue_shopping_returns_to_inventory(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.click_continue_shopping()
    time.sleep(1)
    assert "inventory.html" in driver.current_url


# --- Test 7 ---
@pytest.mark.smoke
@pytest.mark.parametrize("username", USERS)
def test_checkout_opens_checkout_step_one(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(2)
    assert "checkout-step-one.html" in driver.current_url


# --- Test 8 ---
@pytest.mark.parametrize("username", USERS)
def test_page_title(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_title() == LABELS["cart_title"]


# --- Test 9 ---
@pytest.mark.parametrize("username", USERS)
def test_column_labels(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_qty_column_label() == LABELS["qty_label"]
    assert cart.get_desc_column_label() == LABELS["desc_label"]


# --- Test 10 ---
@pytest.mark.parametrize("username", USERS)
def test_two_items_both_listed(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_first_item_name_safely() == PRODUCT_DATA[PRODUCT_IDS[0]]["name"]
    assert cart.get_second_item_name_safely() == PRODUCT_DATA[PRODUCT_IDS[1]]["name"]


# --- Test 11 ---
@pytest.mark.parametrize("username", USERS)
def test_empty_cart_lists_no_items(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.is_cart_empty()


# --- Test 12 ---
@pytest.mark.parametrize("username", USERS)
def test_checkout_with_empty_cart_observe(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(2)
    assert "checkout-step-one.html" in driver.current_url


# --- Test 13 ---
@pytest.mark.parametrize("username", USERS)
def test_removing_one_of_two_keeps_other(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.remove_item(PRODUCT_IDS[0])
    time.sleep(1)
    assert cart.get_first_item_name_safely() == PRODUCT_DATA[PRODUCT_IDS[1]]["name"]


# --- Test 14 ---
@pytest.mark.parametrize("username", USERS)
def test_badge_updates_after_removing_on_cart_page(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    assert cart.get_cart_badge_count() == "2"
    cart.remove_item(PRODUCT_IDS[0])
    time.sleep(1)
    assert cart.get_cart_badge_count() == "1"


# --- Test 15 ---
@pytest.mark.parametrize("username", USERS)
def test_items_retained_after_leaving_and_returning(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.click_continue_shopping()
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    assert cart.get_item_name() == PRODUCT_DATA[PRODUCT_IDS[0]]["name"]
