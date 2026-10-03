import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage, CartPage, CheckoutPage
from data import USERS, PRODUCT_IDS, PRODUCT_DATA, PRODUCT_TOTALS, CHECKOUT_INFO, MESSAGES, LABELS


def _login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(3)


def _go_to_checkout_step_one(driver, username, product=None):
    _login(driver, username)
    inventory = InventoryPage(driver)
    prod = product or PRODUCT_IDS[0]
    inventory.add_item_to_cart(prod)
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(2)


def _go_to_checkout_overview(driver, username, product=None):
    _go_to_checkout_step_one(driver, username, product)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(2)


def _complete_full_order(driver, username, product=None):
    _go_to_checkout_overview(driver, username, product)
    checkout = CheckoutPage(driver)
    checkout.click_finish()
    time.sleep(2)


# ============================================================
# Step One Tests (19 tests, 23 cases)
# ============================================================

# --- Test 1 ---
@pytest.mark.parametrize("username", USERS)
def test_all_fields_filled_goes_to_overview(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 2 ---
@pytest.mark.parametrize("username", USERS)
def test_first_name_missing_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(1)
    assert MESSAGES["checkout_first_name_required"] in checkout.get_error_text()


# --- Test 3 ---
@pytest.mark.parametrize("username", USERS)
def test_last_name_missing_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(1)
    assert MESSAGES["checkout_last_name_required"] in checkout.get_error_text()


# --- Test 4 ---
@pytest.mark.parametrize("username", USERS)
def test_zip_missing_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.click_continue()
    time.sleep(1)
    assert MESSAGES["checkout_postal_code_required"] in checkout.get_error_text()


# --- Test 5 ---
@pytest.mark.parametrize("username", USERS)
def test_first_and_last_missing_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_zip(CHECKOUT_INFO["postal_code"])
    checkout.click_continue()
    time.sleep(1)
    assert MESSAGES["checkout_first_name_required"] in checkout.get_error_text()


# --- Test 6 ---
@pytest.mark.parametrize("username", USERS)
def test_first_and_zip_missing_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_last_name(CHECKOUT_INFO["last_name"])
    checkout.click_continue()
    time.sleep(1)
    assert MESSAGES["checkout_first_name_required"] in checkout.get_error_text()


# --- Test 7 ---
@pytest.mark.parametrize("username", USERS)
def test_last_and_zip_missing_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name(CHECKOUT_INFO["first_name"])
    checkout.click_continue()
    time.sleep(1)
    assert MESSAGES["checkout_last_name_required"] in checkout.get_error_text()


# --- Test 8 ---
@pytest.mark.parametrize("username", USERS)
def test_all_missing_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.click_continue()
    time.sleep(1)
    assert MESSAGES["checkout_first_name_required"] in checkout.get_error_text()


# --- Test 9 ---
@pytest.mark.parametrize("username", USERS)
def test_special_characters_in_names_accepted(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name("!@#$")
    checkout.enter_last_name("%^&*")
    checkout.enter_zip("12345")
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 10 ---
@pytest.mark.parametrize("username", USERS)
def test_numbers_in_names_accepted(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name("123")
    checkout.enter_last_name("456")
    checkout.enter_zip("12345")
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 11 ---
@pytest.mark.parametrize("username", USERS)
def test_letters_in_zip_accepted(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name("John")
    checkout.enter_last_name("Doe")
    checkout.enter_zip("ABCDE")
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 12 ---
@pytest.mark.parametrize("username", USERS)
def test_very_long_input_accepted(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name("a" * 100)
    checkout.enter_last_name("b" * 100)
    checkout.enter_zip("c" * 100)
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 13 ---
@pytest.mark.parametrize("username", USERS)
def test_whitespace_only_first_name_observe(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name("   ")
    checkout.enter_last_name("Doe")
    checkout.enter_zip("12345")
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 14 ---
@pytest.mark.parametrize("username", USERS)
def test_values_stay_in_fields_after_error(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.enter_first_name("John")
    checkout.enter_zip("12345")
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_first_name_value() == "John"
    assert checkout.get_zip_value() == "12345"


# --- Test 15 ---
@pytest.mark.parametrize("field_name", ["first_name", "last_name", "zip"])
@pytest.mark.parametrize("username", USERS)
def test_field_keeps_what_was_typed(driver, username, field_name):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    if field_name == "first_name":
        checkout.enter_first_name("John")
        assert checkout.get_first_name_value() == "John"
    elif field_name == "last_name":
        checkout.enter_last_name("Doe")
        assert checkout.get_last_name_value() == "Doe"
    else:
        checkout.enter_zip("12345")
        assert checkout.get_zip_value() == "12345"


# --- Test 16 ---
@pytest.mark.parametrize("username", USERS)
def test_error_x_button_closes_message(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.click_continue()
    time.sleep(1)
    assert checkout.get_error_text() != ""
    checkout.click_error_close()
    time.sleep(1)
    assert checkout.get_error_text_safely() == ""


# --- Test 17 ---
@pytest.mark.parametrize("field_name", ["first_name", "last_name", "zip"])
@pytest.mark.parametrize("username", USERS)
def test_checkout_step_one_placeholders(driver, username, field_name):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    if field_name == "first_name":
        assert checkout.get_first_name_placeholder() == "First Name"
    elif field_name == "last_name":
        assert checkout.get_last_name_placeholder() == "Last Name"
    else:
        assert checkout.get_zip_placeholder() == "Zip/Postal Code"


# --- Test 18 ---
@pytest.mark.parametrize("username", USERS)
def test_checkout_step_one_title(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    assert checkout.get_title() == LABELS["checkout_step_one_title"]


# --- Test 19 ---
@pytest.mark.parametrize("username", USERS)
def test_cancel_step_one_returns_to_cart(driver, username):
    _go_to_checkout_step_one(driver, username)
    checkout = CheckoutPage(driver)
    checkout.click_cancel()
    time.sleep(1)
    assert "cart.html" in driver.current_url


# ============================================================
# Overview Tests (16 tests, 41 cases)
# ============================================================

# --- Test 20 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_overview_item_name(driver, username, product):
    _go_to_checkout_overview(driver, username, product)
    checkout = CheckoutPage(driver)
    assert checkout.get_overview_item_name() == PRODUCT_DATA[product]["name"]


# --- Test 21 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_overview_item_price(driver, username, product):
    _go_to_checkout_overview(driver, username, product)
    checkout = CheckoutPage(driver)
    assert checkout.get_overview_item_price() == PRODUCT_DATA[product]["price"]


# --- Test 22 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_overview_item_total(driver, username, product):
    _go_to_checkout_overview(driver, username, product)
    checkout = CheckoutPage(driver)
    assert PRODUCT_TOTALS[product]["subtotal"] in checkout.get_item_total()


# --- Test 23 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_overview_tax(driver, username, product):
    _go_to_checkout_overview(driver, username, product)
    checkout = CheckoutPage(driver)
    assert PRODUCT_TOTALS[product]["tax"] in checkout.get_tax()


# --- Test 24 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_overview_total(driver, username, product):
    _go_to_checkout_overview(driver, username, product)
    checkout = CheckoutPage(driver)
    assert PRODUCT_TOTALS[product]["total"] in checkout.get_total()


# --- Test 25 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_title(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    assert checkout.get_title() == LABELS["checkout_step_two_title"]


# --- Test 26 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_payment_info_label(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    assert "Payment Information" in checkout.get_payment_label()


# --- Test 27 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_payment_value(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    assert LABELS["payment_value"] in checkout.get_payment_value()


# --- Test 28 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_shipping_info_label(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    assert "Shipping Information" in checkout.get_shipping_label()


# --- Test 29 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_shipping_value(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    assert LABELS["shipping_value"] in checkout.get_shipping_value()


# --- Test 30 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_quantity(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    assert checkout.get_overview_item_quantity() == "1"


# --- Test 31 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_description_shown(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    assert checkout.get_overview_item_description() != ""


# --- Test 32 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_totals_two_items(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
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
    assert "Item total: $39.98" in checkout.get_item_total()
    assert "Tax: $3.20" in checkout.get_tax()
    assert "Total: $43.18" in checkout.get_total()


# --- Test 33 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_totals_all_six_items(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    for pid in PRODUCT_IDS:
        inventory.add_item_to_cart(pid)
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
    assert "Item total: $129.94" in checkout.get_item_total()
    assert "Tax: $10.40" in checkout.get_tax()
    assert "Total: $140.34" in checkout.get_total()


# --- Test 34 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_cancel_returns_to_inventory(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    checkout.click_cancel()
    time.sleep(1)
    assert "inventory.html" in driver.current_url


# --- Test 35 ---
@pytest.mark.parametrize("username", USERS)
def test_overview_finish_completes_order(driver, username):
    _go_to_checkout_overview(driver, username)
    checkout = CheckoutPage(driver)
    checkout.click_finish()
    time.sleep(1)
    assert "checkout-complete.html" in driver.current_url


# ============================================================
# Complete Tests (8 tests, 8 cases)
# ============================================================

# --- Test 36 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_title(driver, username):
    _complete_full_order(driver, username)
    checkout = CheckoutPage(driver)
    assert checkout.get_title() == LABELS["checkout_complete_title"]


# --- Test 37 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_thank_you_message(driver, username):
    _complete_full_order(driver, username)
    checkout = CheckoutPage(driver)
    assert checkout.get_complete_header() == MESSAGES["checkout_complete_header"]


# --- Test 38 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_dispatched_subtext(driver, username):
    _complete_full_order(driver, username)
    checkout = CheckoutPage(driver)
    assert "dispatched" in checkout.get_complete_text()


# --- Test 39 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_pony_express_image_src(driver, username):
    _complete_full_order(driver, username)
    checkout = CheckoutPage(driver)
    assert LABELS["pony_express_img"] in checkout.get_pony_express_src()


# --- Test 40 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_back_home_returns_to_inventory(driver, username):
    _complete_full_order(driver, username)
    checkout = CheckoutPage(driver)
    checkout.click_back_home()
    time.sleep(1)
    assert "inventory.html" in driver.current_url


# --- Test 41 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_badge_cleared_after_order(driver, username):
    _complete_full_order(driver, username)
    checkout = CheckoutPage(driver)
    assert checkout.get_cart_badge_count() == "0"


# --- Test 42 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_cart_empty_after_back_home(driver, username):
    _complete_full_order(driver, username)
    checkout = CheckoutPage(driver)
    checkout.click_back_home()
    time.sleep(1)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    assert cart.is_cart_empty()


# --- Test 43 ---
@pytest.mark.parametrize("username", USERS)
def test_complete_url(driver, username):
    _complete_full_order(driver, username)
    assert "checkout-complete.html" in driver.current_url
