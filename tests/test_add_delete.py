from playwright.sync_api import sync_playwright


def test_count_added_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        page.wait_for_load_state("domcontentloaded")

        assert "The Internet" in page.title()
        assert "Add/Remove Elements" in page.locator("h3").inner_text()
        assert page.locator("#content > div > button").is_visible()
        assert "Add Element" in page.locator("#content > div > button").inner_text()

        for _ in range(5):
            page.locator("#content > div > button").click()

        assert 5 == page.locator("#elements > button").count()

        for n in range(3):
            page.locator("#elements > button").nth(n).click()

        assert 2 == page.locator("#elements > button").count()

        browser.close()