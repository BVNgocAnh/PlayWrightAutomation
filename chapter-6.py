from playwright.sync_api import sync_playwright
from time import perf_counter


def waiting_to_do_action():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://demoqa.com/automation-practice-form")

        # Simulate the case: can not find the element => timeout 2000ms exceeded. ~ 20
        page.locator("//span[text()='Text Box']").click(timeout=2000)

        # Element is not visible, get locator but not visible to click
        page.locator("//span[text()='Text Box']").click(force=True)
        page.close()


def waiting_until_types():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        ## wait_until = load => load all contents of page: image, ...
        # print ("=================================== START =======================================")
        # start_time = perf_counter()
        # # Load to page
        # page.goto("https://demoqa.com/automation-practice-form", wait_until='load')
        # # Loaded
        # time_taken = perf_counter() - start_time
        # print(f"Page is loaded  in {round(time_taken, 2)}")

        ## wait_until = domcontentloaded => load html, dom only ... no wait all static content
        # print("=================================== START =======================================")
        # start_time = perf_counter()
        # # Load to page
        # page.goto("https://demoqa.com/automation-practice-form", wait_until = 'domcontentloaded')
        # # Loaded
        # time_taken = perf_counter() - start_time
        # print(f"Page is loaded  in {round(time_taken, 2)}")

        ## wait_until = commit => Send request to server and instantly receive response to do next
        # print("=================================== START =======================================")
        # start_time = perf_counter()
        # # Load to page
        # page.goto("https://demoqa.com/automation-practice-form", wait_until='commit')
        # # Loaded
        # time_taken = perf_counter() - start_time
        # print(f"Page is loaded  in {round(time_taken, 2)}")

        # wait_until = networkidle => wait untile network in browser idle
        print(
            "=================================== START ======================================="
        )
        start_time = perf_counter()
        # Load to page
        page.goto(
            "https://demoqa.com/automation-practice-form", wait_until="networkidle"
        )
        # Loaded
        time_taken = perf_counter() - start_time
        print(f"Page is loaded  in {round(time_taken, 2)}")


def waiting_for_element():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=600)
        page = browser.new_page()
        page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

        page.locator("//a[@id='2015']").click()

        print("========== START WAIT ==========")
        start_time = perf_counter()

        title = page.locator("//*[@id='table-body']/tr/td[1]").first
        title.wait_for(timeout=3000)
        title.click()

        time_taken = perf_counter() - start_time

        print(f"Page is loaded  in {round(time_taken, 2)}")


if __name__ == "__main__":
    waiting_for_element()
