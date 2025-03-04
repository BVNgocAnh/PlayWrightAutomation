import asyncio
import getpass
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright, Playwright

#================================ASYNCHRONOUS==================================
async def login(playwright: Playwright):
    username = ""
    password = getpass.getpass("Input password:")

    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("link")
    await page.fill("username", username)
    await page.fill("password", password)
    await page.click("#btn")
    await asyncio.sleep(20)
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await login(playwright)

asyncio.run(main())
#ABC
#================================SYNCHRONOUS==================================
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto("https://playwright.dev/")

#     docs_link = page.get_by_role(role="link", name="Docs")
#     docs_link.click()
    
#     print("Docs:", page.url)
#==============================================================================



