import asyncio
from playwright.async_api import async_playwright, Playwright

async def locator(playwright: Playwright):
    usernameDefault = "standard_user"
    passwordDefault =  "secret_sauce"

    browser = await playwright.chromium.launch(headless=False, slow_mo=600)
    page = await browser.new_page()
    await page.goto("https://bootswatch.com/default/")

    example1 = page.locator('//*[@id="navbarColor01"]/form/input')
    await example1.highlight()

    example2 = page.locator('input.form-control.me-sm-2')
    await example2.highlight()

    await asyncio.sleep(10)
    await page.close()

# - [page.getByRole()](https://playwright.dev/docs/locators#locate-by-role) to locate by explicit and implicit accessibility attributes.
# - [page.getByText()](https://playwright.dev/docs/locators#locate-by-text) to locate by text content.
# - [page.getByLabel()](https://playwright.dev/docs/locators#locate-by-label) to locate a form control by associated label's text.
# - [page.getByPlaceholder()](https://playwright.dev/docs/locators#locate-by-placeholder) to locate an input by placeholder.
# - [page.getByAltText()](https://playwright.dev/docs/locators#locate-by-alt-text) to locate an element, usually image, by its text alternative.
# - [page.getByTitle()](https://playwright.dev/docs/locators#locate-by-title) to locate an element by its title attribute.
# - [page.getByTestId()](https://playwright.dev/docs/locators#locate-by-test-id) to locate an element based on its `data-testid` attribute (other attributes can be configured).
# - page.byXpath(): [Xpath cheatsheet](https://devhints.io/xpath)

async def main():
    async with async_playwright() as playwright:
        await locator(playwright)

asyncio.run(main())