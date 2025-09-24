from playwright.sync_api import sync_playwright


def test_login_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # True = bez GUI, False = widać przeglądarkę
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        # Sprawdzamy, czy w tytule strony pojawia się słowo "Login"
        assert "Internet" in page.title()
        assert "Login" in page.locator("button.radius").inner_text()
        browser.close()


def test_log_in():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.locator("button.radius").click()
        assert 'You logged into a secure area!' in page.locator("#flash").inner_text()
        assert 'Secure Area' in page.locator("#content > div > h2").inner_text()
        assert 'Welcome to the Secure Area. When you are done click logout below.' in page.locator("#content > div > h4").inner_text()
        assert "Logout" in page.locator("""//*[@id="content"]/div/a""").inner_text()

        page.locator("""//*[@id="content"]/div/a""").click()
        assert 'You logged out of the secure area!' in page.locator("#flash").inner_text()

        browser.close()


def test_log_in_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "SyrKonrad")
        page.fill("#password", "123!")
        page.locator("button.radius").click()
        assert 'Your username is invalid!' in page.locator("#flash").inner_text()
        bg_color = page.locator("#flash").evaluate("el => getComputedStyle(el).backgroundColor")
        assert bg_color == "rgb(93, 164, 35)"
        
        browser.close()