from playwright.sync_api import sync_playwright, expect

def on_load(page):
    print("Page is loading: ", page)

def on_request(request):
    print("Request is loading: ", request)

def event_handler():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
    #    page.on("domcontentloaded", on_load)
        page.on("request", on_request)
    
        page.goto("https://demoqa.com/automation-practice-form", wait_until="domcontentloaded") 
        page.close()


def on_event_chooser_file(file_chooser):
    print("Choosing a file")
    file_chooser.set_files("./image/wall.jpg")


def on_event_handler_upload_file():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.on("filechooser", on_event_chooser_file)
        page.goto("https://www.google.com/")

        page.locator("//div[@class='nDcEnd']").click()
        page.locator("//span[@class='DV7the']").click()
        page.close()


def handle_accept_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.accept()
    print("Accept successfully")

def handle_cancel_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.dismiss()
    print("Cancel successfully")

def on_event_handler_alert():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        # page.on("dialog", handle_accept_alert)
        # page.on("dialog", handle_cancel_alert )
        # page.on("dialog", lambda dialog: dialog.dismiss())
        page.on("dialog", lambda dialog:dialog.accept("Automation Testing"))

        page.goto("https://demoqa.com/alerts", wait_until="domcontentloaded", timeout=60000)

        # page.locator("//button[@id='alertButton']").click()
        # page.locator("//button[@id='confirmButton']").click()
        page.locator("//button[@id='promtButton']").click()
        expect(page.locator("//span[@id='promptResult']")).to_contain_text("Automation Testing")

        page.close()
        
if __name__ == "__main__":
    on_event_handler_alert()