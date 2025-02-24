from playwright.sync_api import sync_playwright

def on_load(page):
    print("Page is loading: ", page)

def on_request(request):
    print("Request is loading: ", request)

def event_handler():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        # page.on("load", on_load)

        page.on("request", on_request)
        page.goto("https://demoqa.com/automation-practice-form")
        page.close()

def event_handler():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        # page.on("load", on_load)

        page.on("request", on_request)
        page.goto("https://demoqa.com/automation-practice-form")
        page.close()


def on_event_chooser_file(file_chooser):
    print("Choosing a file")
    file_chooser.set_files("./data/impostor-background.png")


def on_event_handler_upload_file():
    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.on("filechooser", on_event_chooser_file)
        page.goto("https://www.google.com/")

        page.locator("//div[@class='nDcEnd']").click()
        page.close()

if __name__ == "__main__":
    on_event_handler_upload_file()