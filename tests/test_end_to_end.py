import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage, CartPage, CheckoutPage
from data import USERS, PRODUCT_IDS, CHECKOUT_INFO, MESSAGES, LABELS


def _login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(2)


# --- Test 1 ---
@pytest.mark.smoke
@pytest.mark.parametrize("username", USERS)
def test_happy_path_end_to_end(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(1)
    checkout.click_finish()
    time.sleep(1)
    assert checkout.get_complete_header() == MESSAGES["checkout_complete_header"]
    checkout.click_back_home()
    time.sleep(1)
    assert "inventory.html" in driver.current_url
    assert inventory.get_cart_badge_count() == "0"


# --- Test 2 ---
@pytest.mark.parametrize("username", USERS)
def test_checkout_with_three_items(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
    inventory.add_item_to_cart(PRODUCT_IDS[2])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(1)
    checkout.click_finish()
    time.sleep(1)
    assert checkout.get_complete_header() == MESSAGES["checkout_complete_header"]


# --- Test 3 ---
@pytest.mark.parametrize("username", USERS)
def test_cancel_at_step_one_return_to_cart_then_complete(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    checkout.click_cancel()
    time.sleep(1)
    assert "cart.html" in driver.current_url
    cart.click_checkout()
    time.sleep(1)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(1)
    checkout.click_finish()
    time.sleep(1)
    assert checkout.get_complete_header() == MESSAGES["checkout_complete_header"]


# --- Test 4 ---
@pytest.mark.parametrize("username", USERS)
def test_logout_then_login_again(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(1)
    inventory.click_logout()
    time.sleep(1)
    assert "https://www.saucedemo.com/" in driver.current_url
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(2)
    assert "inventory.html" in driver.current_url


# --- Test 5 ---
@pytest.mark.parametrize("username", USERS)
def test_open_checkout_step_two_directly_with_empty_cart_observe(driver, username):
    _login(driver, username)
    checkout = CheckoutPage(driver)
    checkout.load_step_two()
    time.sleep(1)
    assert "checkout-step-two.html" in driver.current_url
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 6 ---
@pytest.mark.parametrize("username", USERS)
def test_open_checkout_complete_directly_observe(driver, username):
    _login(driver, username)
    checkout = CheckoutPage(driver)
    checkout.load_complete()
    time.sleep(1)
    assert "checkout-complete.html" in driver.current_url
    assert checkout.get_complete_header() == MESSAGES["checkout_complete_header"]
