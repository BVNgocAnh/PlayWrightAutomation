import asyncio
from playwright.async_api import async_playwright, Playwright, expect
from pathlib import Path

async def viewport(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()

    await page.set_viewport_size({"width": 1920, "height": 1080})
    await page.goto("https://demoqa.com/links")
    ###https://whatismyviewport.com/

    await page.close()


async def fullscreen(playwright: Playwright):
    user_dir = Path('tmp') / 'playwright'
    user_dir.mkdir(parents=True, exist_ok=True)

    chromium = playwright.chromium
    browser = await chromium.launch_persistent_context(str(user_dir), headless=False, slow_mo=1000, args=['--start-maximized'], no_viewport=True)
    page = await browser.new_page()

    # await page.set_viewport_size({"width": 1920, "height": 1080})
    await page.goto("https://demoqa.com/links")

    link_test = page.locator("//a[@id='simpleLink']")
    await link_test.highlight()    
    await expect(link_test).to_have_text("Home")
    await link_test.click()

    await asyncio.sleep(10)

async def main():
    async with async_playwright() as playwright:
        await fullscreen(playwright)

asyncio.run(main())