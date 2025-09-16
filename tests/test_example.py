from playwright.sync_api import sync_playwright


def test_login_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # True = bez GUI, False = widać przeglądarkę
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        # Sprawdzamy, czy w tytule strony pojawia się słowo "Login"
        assert "Internet" in page.title()

        browser.close()