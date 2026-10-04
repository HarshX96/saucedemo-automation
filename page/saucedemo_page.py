from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
        self.error_close_button = (By.CLASS_NAME, "error-button")
        self.login_logo = (By.CLASS_NAME, "login_logo")
        self.credentials_block = (By.ID, "login_credentials")
        self.password_block = (By.CLASS_NAME, "login_password")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_error_close(self):
        self.driver.find_element(*self.error_close_button).click()

    def get_error_text(self):
        return self.driver.find_element(*self.error_message).text

    def get_error_text_safely(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return ""

    def get_logo_text(self):
        return self.driver.find_element(*self.login_logo).text

    def get_password_field_type(self):
        return self.driver.find_element(*self.password_field).get_attribute("type")

    def get_credentials_text(self):
        return self.driver.find_element(*self.credentials_block).text

    def get_password_block_text(self):
        return self.driver.find_element(*self.password_block).text

    def get_username_placeholder(self):
        return self.driver.find_element(*self.username_field).get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.driver.find_element(*self.password_field).get_attribute("placeholder")

    def get_login_button_value(self):
        return self.driver.find_element(*self.login_button).get_attribute("value")

    def get_username_value(self):
        return self.driver.find_element(*self.username_field).get_attribute("value")

    def get_password_value(self):
        return self.driver.find_element(*self.password_field).get_attribute("value")


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CLASS_NAME, "title")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.active_sort_option = (By.CLASS_NAME, "active_option")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.burger_menu_btn = (By.ID, "react-burger-menu-btn")
        self.close_menu_btn = (By.ID, "react-burger-cross-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.reset_link = (By.ID, "reset_sidebar_link")
        self.all_items_link = (By.ID, "inventory_sidebar_link")
        self.about_link = (By.ID, "about_sidebar_link")
        self.menu_wrap = (By.CLASS_NAME, "bm-menu-wrap")
        self.first_item_name_el = (By.CSS_SELECTOR, ".inventory_item_name")
        self.first_item_price_el = (By.CSS_SELECTOR, ".inventory_item_price")
        self.first_item_image_el = (By.CSS_SELECTOR, "img.inventory_item_img")
        self.last_item_name_el = (By.XPATH, "(//div[contains(@class,'inventory_item_name')])[last()]")
        self.sixth_item_name_el = (By.XPATH, "(//div[contains(@class,'inventory_item_name')])[6]")
        self.seventh_item_name_el = (By.XPATH, "(//div[contains(@class,'inventory_item_name')])[7]")
        self.header_logo = (By.CLASS_NAME, "app_logo")
        self.footer_text_el = (By.CLASS_NAME, "footer_copy")
        self.twitter_link = (By.CSS_SELECTOR, "[data-test='social-x']")
        self.facebook_link = (By.CSS_SELECTOR, "[data-test='social-facebook']")
        self.linkedin_link = (By.CSS_SELECTOR, "[data-test='social-linkedin']")

    def load(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def get_title(self):
        return self.driver.find_element(*self.page_title).text

    def sort_by(self, value):
        Select(self.driver.find_element(*self.sort_dropdown)).select_by_value(value)

    def get_active_sort_option_text(self):
        return self.driver.find_element(*self.active_sort_option).text

    def get_cart_badge_count(self):
        try:
            return self.driver.find_element(*self.cart_badge).text
        except:
            return "0"

    def get_cart_badge_text_safely(self):
        try:
            return self.driver.find_element(*self.cart_badge).text
        except:
            return ""

    def click_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def click_burger_menu(self):
        self.driver.find_element(*self.burger_menu_btn).click()

    def close_burger_menu(self):
        self.driver.find_element(*self.close_menu_btn).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_link).click()

    def click_reset(self):
        self.driver.find_element(*self.reset_link).click()

    def click_all_items(self):
        self.driver.find_element(*self.all_items_link).click()

    def click_about(self):
        self.driver.find_element(*self.about_link).click()

    def get_about_href(self):
        return self.driver.find_element(*self.about_link).get_attribute("href")

    def get_about_target(self):
        return self.driver.find_element(*self.about_link).get_attribute("target")

    def get_menu_link_text(self, link_id):
        return self.driver.find_element(By.ID, link_id).text

    def get_menu_aria_hidden(self):
        return self.driver.find_element(*self.menu_wrap).get_attribute("aria-hidden")

    def add_item_to_cart(self, item_id):
        self.driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

    def remove_item(self, item_id):
        self.driver.find_element(By.ID, f"remove-{item_id}").click()

    def get_first_item_name(self):
        return self.driver.find_element(*self.first_item_name_el).text

    def get_last_item_name(self):
        return self.driver.find_element(*self.last_item_name_el).text

    def get_first_item_price(self):
        return self.driver.find_element(*self.first_item_price_el).text

    def get_first_item_image_src(self):
        return self.driver.find_element(*self.first_item_image_el).get_attribute("src")

    def get_sixth_item_name_safely(self):
        try:
            return self.driver.find_element(*self.sixth_item_name_el).text
        except:
            return ""

    def get_seventh_item_name_safely(self):
        try:
            return self.driver.find_element(*self.seventh_item_name_el).text
        except:
            return ""

    def click_item(self, item_name):
        self.driver.find_element(
            By.XPATH, f"//div[contains(@class,'inventory_item_name') and text()='{item_name}']/parent::a"
        ).click()

    def click_product_name(self, product_id):
        self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//a[contains(@id, 'title_link')]"
        ).click()

    def click_product_image(self, product_id):
        self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//a[contains(@id, 'img_link')]"
        ).click()

    def get_item_button_text(self, item_id):
        try:
            return self.driver.find_element(By.ID, f"add-to-cart-{item_id}").text
        except:
            return self.driver.find_element(By.ID, f"remove-{item_id}").text

    def get_product_name(self, product_id):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//div[contains(@class,'inventory_item_name')]"
        ).text

    def get_product_price(self, product_id):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//div[contains(@class,'inventory_item_price')]"
        ).text

    def get_product_description(self, product_id):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//div[@data-test='inventory-item-desc']"
        ).text

    def get_product_image_src(self, product_id):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//img[contains(@class,'inventory_item_img')]"
        ).get_attribute("src")

    def get_product_image_alt(self, product_id):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//img[contains(@class,'inventory_item_img')]"
        ).get_attribute("alt")

    def get_product_link_href(self, product_id):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//a[contains(@id, 'title_link')]"
        ).get_attribute("href")

    def get_product_button_text(self, product_id):
        return self.driver.find_element(
            By.XPATH, f"//div[@class='inventory_item'][.//button[contains(@id, '{product_id}')]]//button"
        ).text

    def get_sort_option_text(self, value):
        return self.driver.find_element(By.CSS_SELECTOR, f".product_sort_container option[value='{value}']").text

    def get_header_logo_text(self):
        return self.driver.find_element(*self.header_logo).text

    def get_footer_text(self):
        return self.driver.find_element(*self.footer_text_el).text

    def get_twitter_href(self):
        return self.driver.find_element(*self.twitter_link).get_attribute("href")

    def get_facebook_href(self):
        return self.driver.find_element(*self.facebook_link).get_attribute("href")

    def get_linkedin_href(self):
        return self.driver.find_element(*self.linkedin_link).get_attribute("href")

    def get_twitter_target(self):
        return self.driver.find_element(*self.twitter_link).get_attribute("target")

    def get_facebook_target(self):
        return self.driver.find_element(*self.facebook_link).get_attribute("target")

    def get_linkedin_target(self):
        return self.driver.find_element(*self.linkedin_link).get_attribute("target")


class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_name = (By.CLASS_NAME, "inventory_details_name")
        self.product_price = (By.CLASS_NAME, "inventory_details_price")
        self.product_description = (By.CLASS_NAME, "inventory_details_desc")
        self.product_image = (By.CSS_SELECTOR, ".inventory_details_img_container img")
        self.add_to_cart_btn = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
        self.remove_btn = (By.CSS_SELECTOR, "button[id^='remove']")
        self.back_button = (By.ID, "back-to-products")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.header_logo = (By.CLASS_NAME, "app_logo")
        self.footer_text_el = (By.CLASS_NAME, "footer_copy")

    def load(self):
        self.driver.get("https://www.saucedemo.com/inventory-item.html")

    def load_item(self, item_id):
        self.driver.get(f"https://www.saucedemo.com/inventory-item.html?id={item_id}")

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

    def get_product_name_safely(self):
        try:
            return self.driver.find_element(*self.product_name).text
        except:
            return ""

    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text

    def get_product_description(self):
        return self.driver.find_element(*self.product_description).text

    def get_image_src(self):
        return self.driver.find_element(*self.product_image).get_attribute("src")

    def get_image_alt(self):
        return self.driver.find_element(*self.product_image).get_attribute("alt")

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def click_remove(self):
        self.driver.find_element(*self.remove_btn).click()

    def click_back(self):
        self.driver.find_element(*self.back_button).click()

    def get_button_text(self):
        try:
            return self.driver.find_element(*self.add_to_cart_btn).text
        except:
            return self.driver.find_element(*self.remove_btn).text

    def get_cart_badge_count(self):
        try:
            return self.driver.find_element(*self.cart_badge).text
        except:
            return "0"

    def get_header_logo_text(self):
        return self.driver.find_element(*self.header_logo).text

    def get_footer_text(self):
        return self.driver.find_element(*self.footer_text_el).text


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CLASS_NAME, "title")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.item_description = (By.CLASS_NAME, "inventory_item_desc")
        self.item_quantity = (By.CLASS_NAME, "cart_quantity")
        self.remove_button = (By.CSS_SELECTOR, "button[data-test^='remove']")
        self.continue_shopping_btn = (By.CSS_SELECTOR, "[data-test='continue-shopping']")
        self.checkout_btn = (By.CSS_SELECTOR, "[data-test='checkout']")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.qty_label = (By.CLASS_NAME, "cart_quantity_label")
        self.desc_label = (By.CLASS_NAME, "cart_desc_label")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.first_item_name_el = (By.XPATH, "(//div[contains(@class,'inventory_item_name')])[1]")
        self.second_item_name_el = (By.XPATH, "(//div[contains(@class,'inventory_item_name')])[2]")
        self.header_logo = (By.CLASS_NAME, "app_logo")
        self.footer_text_el = (By.CLASS_NAME, "footer_copy")

    def load(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def get_title(self):
        return self.driver.find_element(*self.page_title).text

    def get_item_name(self):
        return self.driver.find_element(*self.item_name).text

    def get_item_price(self):
        return self.driver.find_element(*self.item_price).text

    def get_item_description(self):
        return self.driver.find_element(*self.item_description).text

    def get_quantity(self):
        return self.driver.find_element(*self.item_quantity).text

    def get_qty_column_label(self):
        return self.driver.find_element(*self.qty_label).text

    def get_desc_column_label(self):
        return self.driver.find_element(*self.desc_label).text

    def click_remove(self):
        self.driver.find_element(*self.remove_button).click()

    def remove_item(self, item_id):
        self.driver.find_element(By.ID, f"remove-{item_id}").click()

    def click_continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_btn).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

    def is_cart_empty(self):
        try:
            self.driver.find_element(*self.cart_items)
            return False
        except:
            return True

    def get_cart_item_name_safely(self):
        try:
            return self.driver.find_element(*self.item_name).text
        except:
            return ""

    def get_first_item_name_safely(self):
        try:
            return self.driver.find_element(*self.first_item_name_el).text
        except:
            return ""

    def get_second_item_name_safely(self):
        try:
            return self.driver.find_element(*self.second_item_name_el).text
        except:
            return ""

    def get_cart_badge_count(self):
        try:
            return self.driver.find_element(*self.cart_badge).text
        except:
            return "0"

    def get_header_logo_text(self):
        return self.driver.find_element(*self.header_logo).text

    def get_footer_text(self):
        return self.driver.find_element(*self.footer_text_el).text


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.cancel_btn = (By.ID, "cancel")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
        self.error_close_button = (By.CLASS_NAME, "error-button")
        self.page_title = (By.CLASS_NAME, "title")
        self.overview_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.overview_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.overview_item_quantity = (By.CLASS_NAME, "cart_quantity")
        self.overview_item_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.payment_label = (By.CSS_SELECTOR, "[data-test='payment-info-label']")
        self.payment_value = (By.CSS_SELECTOR, "[data-test='payment-info-value']")
        self.shipping_label = (By.CSS_SELECTOR, "[data-test='shipping-info-label']")
        self.shipping_value = (By.CSS_SELECTOR, "[data-test='shipping-info-value']")
        self.item_total = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_label = (By.CLASS_NAME, "summary_tax_label")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_btn = (By.ID, "finish")
        self.cancel_overview_btn = (By.ID, "cancel")
        self.complete_header = (By.CLASS_NAME, "complete-header")
        self.complete_text = (By.CLASS_NAME, "complete-text")
        self.back_home_btn = (By.ID, "back-to-products")
        self.pony_express_img = (By.CLASS_NAME, "pony_express")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.header_logo = (By.CLASS_NAME, "app_logo")
        self.footer_text_el = (By.CLASS_NAME, "footer_copy")

    def load(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def load_step_one(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def load_step_two(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def load_complete(self):
        self.driver.get("https://www.saucedemo.com/checkout-complete.html")

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name_field).send_keys(name)

    def enter_last_name(self, name):
        self.driver.find_element(*self.last_name_field).send_keys(name)

    def enter_zip(self, zip_code):
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def click_cancel(self):
        self.driver.find_element(*self.cancel_btn).click()

    def click_error_close(self):
        self.driver.find_element(*self.error_close_button).click()

    def get_error_text(self):
        return self.driver.find_element(*self.error_message).text

    def get_error_text_safely(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return ""

    def get_title(self):
        return self.driver.find_element(*self.page_title).text

    def get_first_name_value(self):
        return self.driver.find_element(*self.first_name_field).get_attribute("value")

    def get_last_name_value(self):
        return self.driver.find_element(*self.last_name_field).get_attribute("value")

    def get_zip_value(self):
        return self.driver.find_element(*self.zip_code_field).get_attribute("value")

    def get_first_name_placeholder(self):
        return self.driver.find_element(*self.first_name_field).get_attribute("placeholder")

    def get_last_name_placeholder(self):
        return self.driver.find_element(*self.last_name_field).get_attribute("placeholder")

    def get_zip_placeholder(self):
        return self.driver.find_element(*self.zip_code_field).get_attribute("placeholder")

    def get_overview_item_name(self):
        return self.driver.find_element(*self.overview_item_name).text

    def get_overview_item_price(self):
        return self.driver.find_element(*self.overview_item_price).text

    def get_overview_item_quantity(self):
        return self.driver.find_element(*self.overview_item_quantity).text

    def get_overview_item_description(self):
        return self.driver.find_element(*self.overview_item_desc).text

    def get_payment_label(self):
        return self.driver.find_element(*self.payment_label).text

    def get_payment_value(self):
        return self.driver.find_element(*self.payment_value).text

    def get_shipping_label(self):
        return self.driver.find_element(*self.shipping_label).text

    def get_shipping_value(self):
        return self.driver.find_element(*self.shipping_value).text

    def get_item_total(self):
        return self.driver.find_element(*self.item_total).text

    def get_tax(self):
        return self.driver.find_element(*self.tax_label).text

    def get_total(self):
        return self.driver.find_element(*self.total_label).text

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()

    def get_complete_header(self):
        return self.driver.find_element(*self.complete_header).text

    def get_complete_text(self):
        return self.driver.find_element(*self.complete_text).text

    def get_pony_express_src(self):
        return self.driver.find_element(*self.pony_express_img).get_attribute("src")

    def click_back_home(self):
        self.driver.find_element(*self.back_home_btn).click()

    def get_cart_badge_count(self):
        try:
            return self.driver.find_element(*self.cart_badge).text
        except:
            return "0"

    def get_header_logo_text(self):
        return self.driver.find_element(*self.header_logo).text

    def get_footer_text(self):
        return self.driver.find_element(*self.footer_text_el).text
