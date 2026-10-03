import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage, ProductDetailPage, CartPage, CheckoutPage
from data import USERS, PRODUCT_IDS, NETWORKS, CHECKOUT_INFO, LABELS


def _login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(2)


# ============================================================
# Header Logo Tests (6 separate tests)
# ============================================================

# --- Test 1 ---
@pytest.mark.parametrize("username", USERS)
def test_header_logo_inventory(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_header_logo_text() == LABELS["app_logo"]


# --- Test 2 ---
@pytest.mark.parametrize("username", USERS)
def test_header_logo_product_detail(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(PRODUCT_IDS[0])
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert detail.get_header_logo_text() == LABELS["app_logo"]


# --- Test 3 ---
@pytest.mark.parametrize("username", USERS)
def test_header_logo_cart(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    assert cart.get_header_logo_text() == LABELS["app_logo"]


# --- Test 4 ---
@pytest.mark.parametrize("username", USERS)
def test_header_logo_checkout_step_one(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    assert checkout.get_header_logo_text() == LABELS["app_logo"]


# --- Test 5 ---
@pytest.mark.parametrize("username", USERS)
def test_header_logo_checkout_step_two(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
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
    assert checkout.get_header_logo_text() == LABELS["app_logo"]


# --- Test 6 ---
@pytest.mark.parametrize("username", USERS)
def test_header_logo_checkout_complete(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
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
    assert checkout.get_header_logo_text() == LABELS["app_logo"]


# ============================================================
# Footer Copyright Tests (6 separate tests)
# ============================================================

# --- Test 7 ---
@pytest.mark.parametrize("username", USERS)
def test_footer_copyright_inventory(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert "Sauce Labs" in inventory.get_footer_text()


# --- Test 8 ---
@pytest.mark.parametrize("username", USERS)
def test_footer_copyright_product_detail(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_product_name(PRODUCT_IDS[0])
    time.sleep(1)
    detail = ProductDetailPage(driver)
    assert "Sauce Labs" in detail.get_footer_text()


# --- Test 9 ---
@pytest.mark.parametrize("username", USERS)
def test_footer_copyright_cart(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    assert "Sauce Labs" in cart.get_footer_text()


# --- Test 10 ---
@pytest.mark.parametrize("username", USERS)
def test_footer_copyright_checkout_step_one(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(1)
    checkout = CheckoutPage(driver)
    assert "Sauce Labs" in checkout.get_footer_text()


# --- Test 11 ---
@pytest.mark.parametrize("username", USERS)
def test_footer_copyright_checkout_step_two(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
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
    assert "Sauce Labs" in checkout.get_footer_text()


# --- Test 12 ---
@pytest.mark.parametrize("username", USERS)
def test_footer_copyright_checkout_complete(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
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
    assert "Sauce Labs" in checkout.get_footer_text()


# ============================================================
# Social Links Tests (2 tests, 6 cases)
# ============================================================

# --- Test 13 ---
@pytest.mark.parametrize("network", list(NETWORKS.keys()))
@pytest.mark.parametrize("username", USERS)
def test_social_link_href(driver, username, network):
    _login(driver, username)
    inventory = InventoryPage(driver)
    if network == "twitter":
        assert "twitter.com/saucelabs" in inventory.get_twitter_href() or "x.com/saucelabs" in inventory.get_twitter_href()
    elif network == "facebook":
        assert "facebook.com/saucelabs" in inventory.get_facebook_href()
    else:
        assert "linkedin.com/company/sauce-labs" in inventory.get_linkedin_href()


# --- Test 14 ---
@pytest.mark.parametrize("network", list(NETWORKS.keys()))
@pytest.mark.parametrize("username", USERS)
def test_social_link_opens_new_tab(driver, username, network):
    _login(driver, username)
    inventory = InventoryPage(driver)
    if network == "twitter":
        assert inventory.get_twitter_target() == "_blank"
    elif network == "facebook":
        assert inventory.get_facebook_target() == "_blank"
    else:
        assert inventory.get_linkedin_target() == "_blank"
