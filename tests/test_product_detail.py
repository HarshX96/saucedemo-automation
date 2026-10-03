import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage, ProductDetailPage
from data import USERS, PRODUCT_IDS, PRODUCT_DATA, LABELS


def _login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(2)


# --- Test 1 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_detail_name(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_product_name() == PRODUCT_DATA[product]["name"]


# --- Test 2 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_detail_price(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_product_price() == PRODUCT_DATA[product]["price"]


# --- Test 3 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_detail_description(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_product_description() == PRODUCT_DATA[product]["description"]


# --- Test 4 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_detail_image_src(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert PRODUCT_DATA[product]["image"] in detail.get_image_src()


# --- Test 5 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_detail_image_alt(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_image_alt() == PRODUCT_DATA[product]["alt"]


# --- Test 6 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_detail_initial_button(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_button_text() == LABELS["add_to_cart_btn"]


# --- Test 7 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_open_by_clicking_image(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_image(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_product_name() == PRODUCT_DATA[product]["name"]


# --- Test 8 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_add_from_detail(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    detail.click_add_to_cart()
    time.sleep(1)
    assert detail.get_cart_badge_count() == "1"
    assert detail.get_button_text() == LABELS["remove_btn"]


# --- Test 9 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_remove_from_detail(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(product)
    time.sleep(1)
    detail = ProductDetailPage(driver)
    detail.click_add_to_cart()
    time.sleep(1)
    detail.click_remove()
    time.sleep(1)
    assert detail.get_cart_badge_count() == "0"
    assert detail.get_button_text() == LABELS["add_to_cart_btn"]


# --- Test 10 ---
@pytest.mark.parametrize("username", USERS)
def test_back_to_products_returns_to_inventory(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(PRODUCT_IDS[0])
    time.sleep(1)
    detail = ProductDetailPage(driver)
    detail.click_back()
    time.sleep(1)
    assert "inventory.html" in driver.current_url


# --- Test 11 ---
@pytest.mark.parametrize("username", USERS)
def test_button_shows_remove_after_adding_on_inventory(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_product_name(PRODUCT_IDS[0])
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_button_text() == LABELS["remove_btn"]


# --- Test 12 ---
@pytest.mark.parametrize("username", USERS)
def test_badge_updates_on_detail_page_after_add(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(PRODUCT_IDS[0])
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_cart_badge_count() == "0"
    detail.click_add_to_cart()
    time.sleep(1)
    assert detail.get_cart_badge_count() == "1"


# --- Test 13 ---
@pytest.mark.parametrize("item_id", ["99", "abc"])
@pytest.mark.parametrize("username", USERS)
def test_invalid_item_id_in_url(driver, username, item_id):
    _login(driver, username)
    detail = ProductDetailPage(driver)
    detail.load_item(item_id)
    time.sleep(1)
    assert detail.get_product_name() == "ITEM NOT FOUND"
