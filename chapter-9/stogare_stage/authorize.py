from playwright.sync_api import sync_playwright
import os

def delete_storage_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print("The file deleted successfully!")
    else:
        print("The file does not exist!")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    delete_storage_file("auth/storage_state.json")
    page.goto("https://www.saucedemo.com/", wait_until="load")

    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()

    page.pause()
    
    context.storage_state(path="auth/storage_state.json")
    context.close()
    print(page.url)
    page.close()