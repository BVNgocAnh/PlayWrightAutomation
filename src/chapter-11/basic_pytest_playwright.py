from playwright.sync_api import Page, sync_playwright
import pytest
import logging

# Create a named logger
logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

# Create a file handler to store logs in a file
file_handler = logging.FileHandler("test_log.log", mode="w")  # 'w' to overwrite, 'a' to append
file_handler.setLevel(logging.INFO)

# Create a log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

# configure igonore ssl
# refer to: https://playwright.dev/python/docs/test-runners
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }

@pytest.fixture(scope="function", autouse=True)
def set_up_page(page: Page):
    logger.info(msg="Configure Our Project")
    # playwright = sync_playwright().start()
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # page = browser.new_page()
    logger.info(msg="Open Browser")
    page.goto("https://www.saucedemo.com/")
    # return page
    yield page
    logger.info(msg="Close Browser")
    page.close()

def test_website_login_standard_user(set_up_page: Page):
    logger.info(msg="Input Username")
    set_up_page.locator("//input[@id='user-name']").fill("standard_user")
    logger.info(msg="Input password")
    set_up_page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    set_up_page.locator("//input[@id='login-button']").click()
    assert set_up_page.locator("//div[@class='app_logo']").is_visible()
    # set_up_page.close()

def test_website_login_performance_glitch_user(set_up_page: Page):
    logger.info(msg="Input Username")
    set_up_page.locator("//input[@id='user-name']").fill("performance_glitch_user")
    logger.info(msg="Input password")
    set_up_page.locator("//input[@id='password']").fill("secret_sauce")
    logger.info(msg="Connect login")
    set_up_page.locator("//input[@id='login-button']").click()
    assert set_up_page.locator("//div[@class='app_logo']").is_visible()
    # set_up_page.close()