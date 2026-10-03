import pytest
import time
from page.saucedemo_page import LoginPage
from data import LOGIN_USERS, MESSAGES, LABELS


# --- Test 1 ---
@pytest.mark.smoke
@pytest.mark.parametrize("username", LOGIN_USERS)
def test_valid_login(driver, username):
    login = LoginPage(driver)
    login.load()
    login.enter_username(username)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(2)
    assert "inventory.html" in driver.current_url


# --- Test 2 ---
def test_locked_out_user(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("locked_out_user")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_locked_out"] in login.get_error_text()


# --- Test 3 ---
def test_wrong_username_wrong_password(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("wrong_user")
    login.enter_password("wrong_password")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 4 ---
def test_valid_username_wrong_password(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user")
    login.enter_password("wrong_password")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 5 ---
def test_wrong_username_valid_password(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("wrong_user")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 6 ---
def test_empty_username(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_username_required"] in login.get_error_text()


# --- Test 7 ---
def test_empty_password(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_password_required"] in login.get_error_text()


# --- Test 8 ---
def test_both_empty(driver):
    login = LoginPage(driver)
    login.load()
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_username_required"] in login.get_error_text()


# --- Test 9 ---
def test_username_wrong_case(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("STANDARD_USER")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 10 ---
def test_password_wrong_case(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user")
    login.enter_password("SECRET_SAUCE")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 11 ---
def test_username_leading_space(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username(" standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 12 ---
def test_password_leading_space(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user")
    login.enter_password(" secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 13 ---
def test_username_special_characters(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user!@#$")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 14 ---
def test_long_username(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("a" * 200)
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(1)
    assert MESSAGES["login_invalid"] in login.get_error_text()


# --- Test 15 ---
def test_error_close_button_hides_message(driver):
    login = LoginPage(driver)
    login.load()
    login.click_login()
    time.sleep(1)
    assert login.get_error_text() != ""
    login.click_error_close()
    time.sleep(1)
    assert login.get_error_text_safely() == ""


# --- Test 16 ---
def test_credentials_retained_after_failed_login(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("wrong_user")
    login.enter_password("wrong_password")
    login.click_login()
    time.sleep(1)
    assert login.get_username_value() == "wrong_user"
    assert login.get_password_value() == "wrong_password"


# --- Test 17 ---
def test_logo_text(driver):
    login = LoginPage(driver)
    login.load()
    assert login.get_logo_text() == LABELS["app_logo"]


# --- Test 18 ---
def test_password_field_masked(driver):
    login = LoginPage(driver)
    login.load()
    assert login.get_password_field_type() == "password"


# --- Test 19 ---
def test_accepted_usernames_block(driver):
    login = LoginPage(driver)
    login.load()
    creds = login.get_credentials_text()
    assert "standard_user" in creds
    assert "locked_out_user" in creds
    assert "problem_user" in creds
    assert "performance_glitch_user" in creds
    assert "error_user" in creds
    assert "visual_user" in creds


# --- Test 20 ---
def test_password_hint_block(driver):
    login = LoginPage(driver)
    login.load()
    assert "secret_sauce" in login.get_password_block_text()


# --- Test 21 ---
def test_username_placeholder(driver):
    login = LoginPage(driver)
    login.load()
    assert login.get_username_placeholder() == "Username"


# --- Test 22 ---
def test_password_placeholder(driver):
    login = LoginPage(driver)
    login.load()
    assert login.get_password_placeholder() == "Password"


# --- Test 23 ---
def test_login_button_text(driver):
    login = LoginPage(driver)
    login.load()
    assert login.get_login_button_value() == LABELS["login_btn"]


# --- Test 24 ---
def test_login_page_url_on_load(driver):
    login = LoginPage(driver)
    login.load()
    assert driver.current_url == "https://www.saucedemo.com/"


# --- Test 25 ---
def test_typed_username_stays_before_submit(driver):
    login = LoginPage(driver)
    login.load()
    login.enter_username("standard_user")
    assert login.get_username_value() == "standard_user"
