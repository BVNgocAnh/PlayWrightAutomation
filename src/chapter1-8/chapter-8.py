import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright, Playwright
from time import perf_counter
async def asynchronus_func(playwright: Playwright):
        browser = await playwright.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()

        start_time1 = perf_counter()

        await page.goto("https://playwright.dev/", wait_until= "load")
        await page.get_by_role(role="link", name="Docs").click()

        time_taken = perf_counter() - start_time1 
        print(f"Asynchronus working time in {round(time_taken, 2)}")

async def main():
    async with async_playwright() as playwright:
          await asynchronus_func(playwright)

asyncio.run(main())


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    start_time2 = perf_counter()

    page.goto("https://playwright.dev/", wait_until= "load")
    page.get_by_role(role="link", name="Docs").click()

    time_taken = perf_counter() - start_time2 

    print(f"Synchronus working time in {round(time_taken, 2)}")

