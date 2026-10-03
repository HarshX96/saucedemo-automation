import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage


SECURITY_PATHS = [
    "/inventory.html",
    "/cart.html",
    "/checkout-step-one.html",
    "/checkout-step-two.html",
    "/checkout-complete.html",
    "/inventory-item.html",
]


# --- Test 1 ---
@pytest.mark.parametrize("path", SECURITY_PATHS)
def test_open_directly_without_login_blocked(driver, path):
    driver.get(f"https://www.saucedemo.com{path}")
    time.sleep(1)
    login = LoginPage(driver)
    expected_error = f"You can only access '{path}' when you are logged in."
    assert expected_error in login.get_error_text()


# --- Test 2 ---
def test_inventory_blocked_after_logout(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(2)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(1)
    inventory.click_logout()
    time.sleep(1)
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(1)
    assert "You can only access '/inventory.html' when you are logged in." in login.get_error_text()


# --- Test 3 ---
def test_cart_blocked_after_logout(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(2)
    inventory = InventoryPage(driver)
    inventory.click_burger_menu()
    time.sleep(1)
    inventory.click_logout()
    time.sleep(1)
    driver.get("https://www.saucedemo.com/cart.html")
    time.sleep(1)
    assert "You can only access '/cart.html' when you are logged in." in login.get_error_text()


# --- Test 4 ---
def test_inventory_blocked_after_failed_locked_out_login(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("locked_out_user")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(1)
    assert "You can only access '/inventory.html' when you are logged in." in login.get_error_text()


# --- Test 5 ---
def test_unknown_url_nonexistent_observe(driver):
    driver.get("https://www.saucedemo.com/nonexistent.html")
    time.sleep(1)
    assert "nonexistent.html" in driver.current_url
