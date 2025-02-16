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

    no_radio = page.locator("//label[@for='noRadio']")
    await no_radio.highlight()
    await expect(page.locator("//label[@for='noRadio']")).not_to_be_checked()
    
    await asyncio.sleep(20)

async def action_table(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/webtables", wait_until="domcontentloaded")

    table = page.locator("//div[@role='columnheader']/div[@class='rt-resizable-header-content']")
    await expect(table).to_have_count(7)
    await expect(table.get_by_text("Department")).to_be_visible()
    await page.close()
    
async def action_button(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/buttons", wait_until="domcontentloaded")

    click_me_button = page.locator("//div[3]/button")
    await click_me_button.highlight()
    await expect(click_me_button).to_be_visible()
    await click_me_button.click()
    
    double_click_button = page.get_by_role("button", name="Double Click Me")
    await double_click_button.highlight()
    await expect(double_click_button).to_be_enabled()
    await double_click_button.dblclick()

    right_click_button = page.get_by_role("button", name="Right Click Me")
    await right_click_button.highlight()
    await right_click_button.click(button='right')

    await page.close()

async def action_link(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/links", wait_until="domcontentloaded")

    link_text = page.locator("//a[@id='simpleLink']")
    await expect(link_text).to_have_text("Home")
    await link_text.click()

    await page.close()

async def action_dropdown1(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/webtables", wait_until="domcontentloaded")

    await page.locator("//div[@class='-center']//select").highlight()
    await page.locator("//div[@class='-center']//select").select_option("8")

    await page.close()

async def action_dropdown2(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/automation-practice-form", wait_until="domcontentloaded")

    await page.locator("//div[@id='state']").click()
    await page.locator("//div[@class=' css-11unzgr']/div").get_by_text("NCR").click()
    await page.locator("//div[@id='state']").click()
    await page.locator("//div[@class=' css-11unzgr']/div").get_by_text("Haryana").click()

    await page.close()

async def action_keyboard_shortcut(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/automation-practice-form")

    # Case: Not a Select Element
    await page.locator("//input[@id='firstName']").fill("TestingEveryoneOne")
    await page.locator("//input[@id='firstName']").fill("")

    await page.locator("//input[@id='firstName']").fill("TestingEveryoneOne")
    await page.locator("//input[@id='firstName']").clear()

    await page.locator("//input[@id='firstName']").press("KeyT")
    await page.locator("//input[@id='firstName']").press("KeyE")
    await page.locator("//input[@id='firstName']").clear()

    await page.locator("//input[@id='firstName']").press("Shift+KeyT")
    await page.locator("//input[@id='firstName']").press("KeyE")
    await page.locator("//input[@id='firstName']").press("KeyS")
    await page.locator("//input[@id='firstName']").press("KeyT")

    await page.locator("//input[@id='firstName']").press("ArrowLeft")

    await page.locator("//input[@id='firstName']").clear()
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await action_keyboard_shortcut(playwright)

asyncio.run(main())