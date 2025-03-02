from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright

load_dotenv()  # Load environment variables from .env

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


def delete_storage_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("The file does not exist.")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo= 500)
    context = browser.new_context()
    page = context.new_page()

    delete_storage_file("./auth/storage_stage.json")

    page.goto("https://accounts.google.com/")


    page.locator("//input[@type='email']").fill(email)
    page.get_by_role("button", name="Next").click()


    page.locator("//input[@type='password']").fill(password)
    page.get_by_role("button", name="Next").click()
    page.pause()

    #### Here is the
    context.storage_state(path="./auth/storage_stage.json")
    context.close()
    print(page.url)
    page.close()
    