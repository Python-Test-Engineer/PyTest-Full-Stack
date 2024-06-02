from playwright.sync_api import sync_playwright


# download event handler
def on_download(download):
    # print("Download received!")
    download.save_as("./screenshots/night.jpg")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/NDRwHCC7JuI")

    # register listener
    page.once("download", on_download)

    btn = page.get_by_role("link", name="Download free")

    # expect download
    with page.expect_download() as download:
        # trigger download
        btn.click()
        # Save using download
        download = download.value
        download.save_as(f"./screenshots/{download.suggested_filename}")

    browser.close()
