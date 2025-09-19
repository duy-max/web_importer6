from locators import login as login_lcts
from corelib.web_handler import WebHandler
from corelib import logger

class Login(WebHandler):
    def __init__(self, page):
        super().__init__(page)
        self.LCT = login_lcts
        self.logger = logger.Logger(prefix="WebHandler", log_level= "INFO")

    def navigate_to_login_page(self, base_url: str):
        self.goto_page(base_url + "/login")
    
    def login_into_website(self, username: str, password: str):
        self.fill_element(self.LCT.USERNAME, username)
        self.fill_element(self.LCT.PASSWORD, password)
        self.click_element(self.LCT.LOGIN_BTN)

    # Dùng asyncio.gather để chạy song song.
    # mở 30 browser cùng 1 lúc
    # async def login_task(user_id):
    #     async with async_playwright() as p:
    #         browser = await p.chromium.launch(headless=True)
    #         page = await browser.new_page()
    #         await page.goto("https://www.google.com")
    #         print(f"User {user_id} - Title: {await page.title()}")
    #         await browser.close()

    # async def main():
    #     tasks = [login_task(i) for i in range(30)]
    #     await asyncio.gather(*tasks)

    # asyncio.run(main())