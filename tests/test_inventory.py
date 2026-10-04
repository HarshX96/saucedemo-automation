import pytest
import time
from page.saucedemo_page import LoginPage, InventoryPage, CartPage
from data import USERS, PRODUCT_IDS, PRODUCT_DATA, SORT_OPTIONS, SORT_EXPECTATIONS, LABELS


def _login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(3)


# --- Product Display Tests (1–10) ---

# --- Test 1 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_product_name(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_product_name(product) == PRODUCT_DATA[product]["name"]


# --- Test 2 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_product_price(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_product_price(product) == PRODUCT_DATA[product]["price"]


# --- Test 3 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_product_description(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_product_description(product) == PRODUCT_DATA[product]["description"]


# --- Test 4 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_product_image_src(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert PRODUCT_DATA[product]["image"] in inventory.get_product_image_src(product)


# --- Test 5 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_product_image_alt(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_product_image_alt(product) == PRODUCT_DATA[product]["alt"]


# --- Test 6 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_product_name_link_href(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_product_link_href(product) == PRODUCT_DATA[product]["detail_link"]


# --- Test 7 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_initial_button_text(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_product_button_text(product) == LABELS["add_to_cart_btn"]


# --- Test 8 ---
@pytest.mark.parametrize("username", USERS)
def test_products_page_title(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_title() == LABELS["inventory_title"]


# --- Test 9 ---
@pytest.mark.parametrize("username", USERS)
def test_exactly_six_products(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_sixth_item_name_safely() != ""
    assert inventory.get_seventh_item_name_safely() == ""


# --- Test 10 ---
@pytest.mark.parametrize("username", USERS)
def test_default_sort_label(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_active_sort_option_text() == SORT_EXPECTATIONS["az"]["label"]


# --- Cart Actions Tests (11–20) ---

# --- Test 11 ---
@pytest.mark.smoke
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_add_product(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(product)
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "1"
    assert inventory.get_item_button_text(product) == LABELS["remove_btn"]


# --- Test 12 ---
@pytest.mark.parametrize("product", PRODUCT_IDS)
@pytest.mark.parametrize("username", USERS)
def test_remove_product(driver, username, product):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(product)
    time.sleep(1)
    inventory.remove_item(product)
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "0"
    assert inventory.get_item_button_text(product) == LABELS["add_to_cart_btn"]


# --- Test 13 ---
@pytest.mark.parametrize("username", USERS)
def test_add_three_items(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
    inventory.add_item_to_cart(PRODUCT_IDS[2])
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "3"


# --- Test 14 ---
@pytest.mark.parametrize("username", USERS)
def test_add_all_six_items(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
    inventory.add_item_to_cart(PRODUCT_IDS[2])
    inventory.add_item_to_cart(PRODUCT_IDS[3])
    inventory.add_item_to_cart(PRODUCT_IDS[4])
    inventory.add_item_to_cart(PRODUCT_IDS[5])
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "6"


# --- Test 15 ---
@pytest.mark.parametrize("username", USERS)
def test_add_two_remove_one(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    inventory.add_item_to_cart(PRODUCT_IDS[1])
    time.sleep(1)
    inventory.remove_item(PRODUCT_IDS[0])
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "1"


# --- Test 16 ---
@pytest.mark.parametrize("username", USERS)
def test_badge_absent_when_cart_empty(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_cart_badge_count() == "0"


# --- Test 17 ---
@pytest.mark.parametrize("username", USERS)
def test_badge_stays_after_cart_round_trip(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    inventory.click_cart()
    time.sleep(2)
    cart = CartPage(driver)
    cart.click_continue_shopping()
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "1"


# --- Test 18 ---
@pytest.mark.parametrize("username", USERS)
def test_reset_app_state_clears_cart(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "1"
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.click_reset()
    time.sleep(1)
    inventory.close_burger_menu()
    time.sleep(1)
    inventory.load()
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "0"


# --- Test 19 ---
@pytest.mark.parametrize("username", USERS)
def test_reset_app_state_reverts_buttons(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart(PRODUCT_IDS[0])
    time.sleep(1)
    assert inventory.get_item_button_text(PRODUCT_IDS[0]) == LABELS["remove_btn"]
    inventory.click_burger_menu()
    time.sleep(2)
    inventory.click_reset()
    time.sleep(1)
    inventory.close_burger_menu()
    time.sleep(1)
    inventory.load()
    time.sleep(1)
    assert inventory.get_item_button_text(PRODUCT_IDS[0]) == LABELS["add_to_cart_btn"]


# --- Test 20 ---
@pytest.mark.smoke
@pytest.mark.parametrize("username", USERS)
def test_cart_icon_opens_cart_page(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.click_cart()
    time.sleep(2)
    assert "cart.html" in driver.current_url


# --- Sorting Tests (21–27) ---

# --- Test 21 ---
@pytest.mark.parametrize("sort_option", SORT_OPTIONS)
@pytest.mark.parametrize("username", USERS)
def test_each_option_text_in_dropdown(driver, username, sort_option):
    _login(driver, username)
    inventory = InventoryPage(driver)
    assert inventory.get_sort_option_text(sort_option) == SORT_EXPECTATIONS[sort_option]["label"]


# --- Test 22 ---
@pytest.mark.parametrize("sort_option", SORT_OPTIONS)
@pytest.mark.parametrize("username", USERS)
def test_selected_label_shows_after_choosing(driver, username, sort_option):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.sort_by(sort_option)
    time.sleep(1)
    assert inventory.get_active_sort_option_text() == SORT_EXPECTATIONS[sort_option]["label"]


# --- Test 23 ---
@pytest.mark.smoke
@pytest.mark.parametrize("sort_option", SORT_OPTIONS)
@pytest.mark.parametrize("username", USERS)
def test_first_item_is_correct(driver, username, sort_option):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.sort_by(sort_option)
    time.sleep(1)
    assert inventory.get_first_item_name() == SORT_EXPECTATIONS[sort_option]["first"]


# --- Test 24 ---
@pytest.mark.parametrize("sort_option", SORT_OPTIONS)
@pytest.mark.parametrize("username", USERS)
def test_last_item_is_correct(driver, username, sort_option):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.sort_by(sort_option)
    time.sleep(1)
    assert inventory.get_last_item_name() == SORT_EXPECTATIONS[sort_option]["last"]


# --- Test 25 ---
@pytest.mark.parametrize("username", USERS)
def test_add_to_cart_after_sorting(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.sort_by("lohi")
    time.sleep(1)
    inventory.add_item_to_cart(PRODUCT_IDS[4])
    time.sleep(1)
    assert inventory.get_cart_badge_count() == "1"


# --- Test 26 ---
@pytest.mark.parametrize("username", USERS)
def test_sort_choice_stays_after_cart_round_trip(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.sort_by("lohi")
    time.sleep(1)
    inventory.click_cart()
    time.sleep(1)
    cart = CartPage(driver)
    cart.click_continue_shopping()
    time.sleep(3)
    assert inventory.get_active_sort_option_text() == SORT_EXPECTATIONS["az"]["label"]
    assert inventory.get_first_item_name() == SORT_EXPECTATIONS["az"]["first"]


# --- Test 27 ---
@pytest.mark.parametrize("username", USERS)
def test_choosing_az_again_restores_default_first_item(driver, username):
    _login(driver, username)
    inventory = InventoryPage(driver)
    inventory.sort_by("za")
    time.sleep(1)
    inventory.sort_by("az")
    time.sleep(1)
    assert inventory.get_first_item_name() == SORT_EXPECTATIONS["az"]["first"]
