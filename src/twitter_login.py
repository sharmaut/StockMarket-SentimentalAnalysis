# login_twitter.py
from playwright.sync_api import sync_playwright

def login_and_save_state():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to Twitter login page
        page.goto("https://twitter.com/login")

        # Give yourself time to manually log in
        input("Log in manually, then press Enter here to continue...")

        # Once logged in, save the session to a file
        context.storage_state(path="twitter_state.json")
        print("Twitter session saved to twitter_state.json")
        browser.close()

if __name__ == "__main__":
    login_and_save_state()
