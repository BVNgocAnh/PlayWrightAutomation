from playwright.sync_api import sync_playwright
import os

def delete_storage_file(filepath):
    if os.path.exists(filepath):
        os.remove()
        print("The file deleted successfully!")
    else:
        print("The file does not exist!")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    context = browser.new_context(storage_state="auth/storage_state.json")
    
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html", wait_until="load")

    page.pause()
    print(page.url)
    page.close()