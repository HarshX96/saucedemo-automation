# SauceDemo QA Automation

An end-to-end test automation suite for [saucedemo.com](https://www.saucedemo.com) built with **Python**, **Selenium**, and **pytest**.  
Tests run on-demand via **GitHub Actions** with parallel execution and selectable user profiles.

---

## Tech Stack

| Tool | Purpose |
|:-----|:--------|
| Python 3.11 | Language |
| Selenium 4 | Browser automation |
| pytest | Test framework |
| pytest-xdist | Parallel test execution |
| pytest-html | HTML test reports |
| GitHub Actions | CI/CD pipeline |
| Page Object Model | Test architecture |

---

## Project Structure

```
saucedemo/
├── .github/
│   └── workflows/
│       └── run_tests.yml       # CI/CD pipeline
├── page/
│   └── saucedemo_page.py       # Page Object Model
├── tests/
│   ├── test_login.py           # 25 test functions
│   ├── test_inventory.py       # 27 test functions
│   ├── test_product_detail.py  # 13 test functions
│   ├── test_cart.py            # 15 test functions
│   ├── test_checkout.py        # 43 test functions
│   ├── test_menu.py            # 8 test functions
│   ├── test_header_footer.py   # 14 test functions
│   ├── test_end_to_end.py      # 6 test functions
│   └── test_security.py        # 5 test functions
├── documents/
│   ├── test_cases.pdf          # 156 test cases
│   └── problem_user_bugs.pdf   # 6 bugs found
├── .gitignore
├── conftest.py                 # Fixtures & browser setup
├── data.py                     # Test data & constants
├── pytest.ini                  # pytest config & markers
└── requirements.txt            # Dependencies
```

---

## Test Coverage

| Module | Test Functions | Total Runs (all users) |
|:-------|:-------------:|:----------------------:|
| Login | 25 | 29 |
| Inventory | 27 | 336 |
| Product Detail | 13 | 236 |
| Cart | 15 | 140 |
| Checkout | 43 | 288 |
| Menu | 8 | 44 |
| Header / Footer | 14 | 72 |
| End to End | 6 | 24 |
| Security | 5 | 10 |
| **Total** | **156** | **1179** |

> Tests are parametrized — the same function runs across multiple users and products, which is why total runs far exceed the number of functions.

---

## Test Users

Tests run across 4 user profiles to validate different app behaviours:

| User | Behaviour |
|:-----|:---------|
| `standard_user` | Normal user — all features work correctly |
| `problem_user` | Broken images, broken sorting, broken checkout — **6 bugs found** |
| `error_user` | Intermittent element errors |
| `visual_user` | Visual layout differences |

> Login tests also include `performance_glitch_user` (slow network simulation).

---

## Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/HarshX96/saucedemo-automation.git
cd saucedemo-automation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run tests

```bash
# Smoke tests only (7 critical tests)
pytest -m smoke

# All tests
pytest

# Specific user
pytest -k "standard_user"
pytest -k "problem_user"

# Parallel execution (4 workers)
pytest -n 4

# With HTML report
pytest -n 4 --html=reports/report.html --self-contained-html
```

---

## CI/CD — GitHub Actions

The workflow is configured for manual execution on-demand from the **Actions** tab.

### Manual run options

| Input | Options |
|:------|:--------|
| **Test suite** | `smoke`, `all`, `standard_user`, `problem_user`, `error_user`, `visual_user`, any combination of users, `rerun_failed` |
| **Parallel workers** | `1` to `10` (default: `4`) |

The HTML report is uploaded as a workflow artifact after every run (kept for 14 days).

---

## Smoke Tests

7 critical tests tagged `@pytest.mark.smoke`:

| Test | What it checks |
|:-----|:--------------|
| `test_valid_login` | Login works for all valid users |
| `test_add_product` | Add to cart works |
| `test_cart_icon_opens_cart_page` | Cart navigation works |
| `test_first_item_is_correct` | Default sort order is correct |
| `test_checkout_opens_checkout_step_one` | Checkout flow starts correctly |
| `test_logout_returns_to_login` | Logout works |
| `test_happy_path_end_to_end` | Full order flow — add → checkout → complete |

---

## Bug Report — problem_user

**6 bugs found, 150 test failures** across inventory, product detail, and checkout modules.

| Bug ID | Title | Severity |
|:-------|:------|:--------:|
| BUG-001 | All product images show same broken placeholder | High |
| BUG-002 | Add to Cart does not work for 3 of 6 products | Critical |
| BUG-003 | Remove button cannot be found after adding product | Critical |
| BUG-004 | Sorting does not reorder products | High |
| BUG-005 | Product detail page elements not found | High |
| BUG-006 | Checkout blocked — Last Name routes keystrokes to First Name field | Critical |

---

## Documentation

| Document | Description |
|:---------|:-----------|
| [`documents/test_cases.pdf`](documents/test_cases.pdf) | 156 test cases with steps, expected results, type and priority |
| [`documents/problem_user_bugs.pdf`](documents/problem_user_bugs.pdf) | 6 bug reports with reproduction steps, severity and failing test list |
