import asyncio
from playwright.async_api import async_playwright, Playwright, expect
from pathlib import Path

async def download(playwright: Playwright):
    user_dir = Path('tmp') / 'playwright'
    user_dir.mkdir(parents=True, exist_ok=True)

    chromium = playwright.chromium
    browser = await chromium.launch_persistent_context(str(user_dir), headless=False, slow_mo=1000, args=['--start-maximized'], no_viewport=True)
    page = await browser.new_page()
    await page.goto('https://demoqa.com/upload-download')

    async with page.expect_download() as download_info:
        await page.locator('//a[@id="downloadButton"]').click()

    download = await download_info.value

    await download.save_as("./new_download_folder/" + download.suggested_filename)
    await page.close()


async def upload(playwright: Playwright):
    user_dir = Path('tmp') / 'playwright'
    user_dir.mkdir(parents=True, exist_ok=True)

    chromium = playwright.chromium
    browser = await chromium.launch_persistent_context(str(user_dir), headless=False, slow_mo=1000, args=['--start-maximized'], no_viewport=True)
    page = await browser.new_page()
    await page.goto('https://demoqa.com/upload-download')

    await page.locator("//input[@id='uploadFile']").set_input_files("./download_folder/sampleFile.jpeg")

    await page.locator("//input[@id='uploadFile']").set_input_files([])

    await page.locator("//input[@id='uploadFile']").set_input_files("./download_folder/sampleFile.jpeg")
    await expect(page.locator("//p[@id='uploadedFilePath']")).to_contain_text("sampleFile.jpeg")
    await page.close()

async def upload_more_file(playwright: Playwright):
    user_dir = Path('tmp') / 'playwright'
    user_dir.mkdir(parents=True, exist_ok=True)

    chromium = playwright.chromium
    browser = await chromium.launch_persistent_context(str(user_dir), headless=False, slow_mo=1000, args=['--start-maximized'], no_viewport=True)
    page = await browser.new_page()

    await page.goto('https://www.google.com/')

    await page.locator("//div[@class='nDcEnd']").click()

    async with page.expect_file_chooser() as fc_info:
        await page.locator("//span[@class='DV7the']").click()

    file_chooser = await fc_info.value
    
    await file_chooser.set_files("./download_folder/sampleFile.jpeg")

    await page.close()

async def main():
    async with async_playwright() as playwright:
        await upload_more_file(playwright)

asyncio.run(main())