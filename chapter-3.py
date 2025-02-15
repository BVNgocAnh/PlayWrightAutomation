import asyncio
from playwright.async_api import async_playwright, Playwright, expect

async def action_textbox(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/text-box")

    fullname_textbox = page.locator("#userName")
    await fullname_textbox.fill("AutomationTesting")

    email_textbox = page.locator("#userEmail")
    await email_textbox.fill("Testing@gmail.com")

    currentAddress_textbox = page.locator("#currentAddress")
    await currentAddress_textbox.fill("Tran Van Hoai")
    await currentAddress_textbox.clear()
    await asyncio.sleep(7)


async def action_checkbox(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/checkbox", wait_until="domcontentloaded")

    folder_checkbox = page.locator(".rct-checkbox")
    await folder_checkbox.highlight()
    await folder_checkbox.click()

    await asyncio.sleep(7)


async def action_radio(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/radio-button", wait_until="domcontentloaded")

    yes_radio = page.locator("//label[@for='yesRadio']")
    await yes_radio.highlight()
    await yes_radio.check()
    assert (await yes_radio.is_checked())


    await expect(page.locator("//label[@for='noRadio']")).not_to_be_checked()
    
    await asyncio.sleep(20)

async def main():
    async with async_playwright() as playwright:
        await action_radio(playwright)

asyncio.run(main())