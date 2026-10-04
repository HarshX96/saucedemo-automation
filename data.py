USERS = [
    "standard_user",
    "problem_user",
    "error_user",
    "visual_user",
]

LOGIN_USERS = [
    "standard_user",
    "performance_glitch_user",
    "problem_user",
    "error_user",
    "visual_user",
]

PRODUCT_IDS = [
    "sauce-labs-backpack",
    "sauce-labs-bike-light",
    "sauce-labs-bolt-t-shirt",
    "sauce-labs-fleece-jacket",
    "sauce-labs-onesie",
    "test.allthethings()-t-shirt-(red)",
]

PRODUCT_DATA = {
    "sauce-labs-backpack": {
        "name": "Sauce Labs Backpack",
        "price": "$29.99",
        "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
        "image": "https://www.saucedemo.com/assets/sauce-backpack-1200x1500-CjRW-Djj.jpg",
        "alt": "Sauce Labs Backpack",
        "detail_link": "https://www.saucedemo.com/inventory.html#",
    },
    "sauce-labs-bike-light": {
        "name": "Sauce Labs Bike Light",
        "price": "$9.99",
        "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
        "image": "https://www.saucedemo.com/assets/bike-light-1200x1500-DxcZRFOA.jpg",
        "alt": "Sauce Labs Bike Light",
        "detail_link": "https://www.saucedemo.com/inventory.html#",
    },
    "sauce-labs-bolt-t-shirt": {
        "name": "Sauce Labs Bolt T-Shirt",
        "price": "$15.99",
        "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
        "image": "https://www.saucedemo.com/assets/bolt-shirt-1200x1500-mR0ldpVS.jpg",
        "alt": "Sauce Labs Bolt T-Shirt",
        "detail_link": "https://www.saucedemo.com/inventory.html#",
    },
    "sauce-labs-fleece-jacket": {
        "name": "Sauce Labs Fleece Jacket",
        "price": "$49.99",
        "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
        "image": "https://www.saucedemo.com/assets/sauce-pullover-1200x1500-BfbI-PSd.jpg",
        "alt": "Sauce Labs Fleece Jacket",
        "detail_link": "https://www.saucedemo.com/inventory.html#",
    },
    "sauce-labs-onesie": {
        "name": "Sauce Labs Onesie",
        "price": "$7.99",
        "description": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
        "image": "https://www.saucedemo.com/assets/red-onesie-1200x1500-BrSuq0ic.jpg",
        "alt": "Sauce Labs Onesie",
        "detail_link": "https://www.saucedemo.com/inventory.html#",
    },
    "test.allthethings()-t-shirt-(red)": {
        "name": "Test.allTheThings() T-Shirt (Red)",
        "price": "$15.99",
        "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.",
        "image": "https://www.saucedemo.com/assets/red-tatt-1200x1500-E-qp6aYf.jpg",
        "alt": "Test.allTheThings() T-Shirt (Red)",
        "detail_link": "https://www.saucedemo.com/inventory.html#",
    },
}

SORT_OPTIONS = ["az", "za", "lohi", "hilo"]

SORT_EXPECTATIONS = {
    "az": {
        "label": "Name (A to Z)",
        "first": "Sauce Labs Backpack",
        "last": "Test.allTheThings() T-Shirt (Red)",
    },
    "za": {
        "label": "Name (Z to A)",
        "first": "Test.allTheThings() T-Shirt (Red)",
        "last": "Sauce Labs Backpack",
    },
    "lohi": {
        "label": "Price (low to high)",
        "first": "Sauce Labs Onesie",
        "last": "Sauce Labs Fleece Jacket",
    },
    "hilo": {
        "label": "Price (high to low)",
        "first": "Sauce Labs Fleece Jacket",
        "last": "Sauce Labs Onesie",
    },
}

MENU_LINKS = {
    "inventory_sidebar_link": "All Items",
    "about_sidebar_link": "About",
    "logout_sidebar_link": "Logout",
    "reset_sidebar_link": "Reset App State",
}

NETWORKS = {
    "twitter": {
        "name": "Twitter/X",
        "href": "https://x.com/saucelabs",
    },
    "facebook": {
        "name": "Facebook",
        "href": "https://www.facebook.com/saucelabs",
    },
    "linkedin": {
        "name": "LinkedIn",
        "href": "https://www.linkedin.com/company/sauce-labs/",
    },
}

CHECKOUT_INFO = {
    "first_name": "John",
    "last_name": "Doe",
    "postal_code": "12345",
}

MESSAGES = {
    "login_locked_out": "Sorry, this user has been locked out.",
    "login_invalid": "Username and password do not match any user in this service",
    "login_username_required": "Username is required",
    "login_password_required": "Password is required",
    "checkout_first_name_required": "First Name is required",
    "checkout_last_name_required": "Last Name is required",
    "checkout_postal_code_required": "Postal Code is required",
    "checkout_complete_header": "Thank you for your order!",
    "checkout_complete_text": "Your order has been dispatched, and will arrive just as fast as the pony can get there!",
}

LABELS = {
    "app_logo": "Swag Labs",
    "inventory_title": "Products",
    "cart_title": "Your Cart",
    "checkout_step_one_title": "Checkout: Your Information",
    "checkout_step_two_title": "Checkout: Overview",
    "checkout_complete_title": "Checkout: Complete!",
    "qty_label": "QTY",
    "desc_label": "Description",
    "payment_info": "Payment Information:",
    "shipping_info": "Shipping Information:",
    "payment_value": "SauceCard #31337",
    "shipping_value": "Free Pony Express Delivery!",
    "add_to_cart_btn": "Add to cart",
    "remove_btn": "Remove",
    "login_btn": "Login",
    "footer_copy": "Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy",
    "pony_express_img": "checkmark-VLWQafip.png",
}

PRODUCT_TOTALS = {
    "sauce-labs-backpack": {"subtotal": "$29.99", "tax": "$2.40", "total": "$32.39"},
    "sauce-labs-bike-light": {"subtotal": "$9.99", "tax": "$0.80", "total": "$10.79"},
    "sauce-labs-bolt-t-shirt": {"subtotal": "$15.99", "tax": "$1.28", "total": "$17.27"},
    "sauce-labs-fleece-jacket": {"subtotal": "$49.99", "tax": "$4.00", "total": "$53.99"},
    "sauce-labs-onesie": {"subtotal": "$7.99", "tax": "$0.64", "total": "$8.63"},
    "test.allthethings()-t-shirt-(red)": {"subtotal": "$15.99", "tax": "$1.28", "total": "$17.27"},
}
