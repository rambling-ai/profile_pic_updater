import asyncio
import sys
import json
from playwright.async_api import async_playwright
from getpass import getpass
import random
import time

COOKIES_FILE_PATH = "cookies.txt"

def sleep_random_time():
    random_time = random.uniform(1, 2)
    time.sleep(random_time)

async def main():
    image_path = sys.argv[1]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        
        # Load cookies if exists
        try:
            with open(COOKIES_FILE_PATH, 'r') as f:
                cookies = json.load(f)
                await context.add_cookies(cookies)
        except FileNotFoundError:
            print("No cookies file found. Proceeding with login.")

        page = await context.new_page()
        await page.goto("https://www.linkedin.com/in/")
        
        # Check if not logged in
        try:
            await page.wait_for_selector(".profile-photo-edit__edit-btn", timeout=5000)
        except:
            print("Please login to your LinkedIn account in the new browser window, then return here and press Enter.")
            getpass("")  # Using getpass to wait for input, without echoing what's entered.
            cookies = await context.cookies()
            with open(COOKIES_FILE_PATH, 'w') as f:
                json.dump(cookies, f)

        await page.click(".profile-photo-edit__edit-btn")

        sleep_random_time()

        await page.click('//button[contains(@class, "artdeco-button--tertiary")]//li-icon[@type="camera"]')

        sleep_random_time()

        input_element = await page.wait_for_selector('#image-selector__file-upload-input')

        sleep_random_time()

        await input_element.set_input_files(image_path)

        sleep_random_time()

        await page.click('button.artdeco-button--primary span.artdeco-button__text:has-text("Save photo")')

        # Wait for page to load
        await page.wait_for_load_state('load')
        
        sleep_random_time()
        
        await browser.close()

asyncio.run(main())
