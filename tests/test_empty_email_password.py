# test_empty_fields.py
from selenium.webdriver.common.by import By
import time
from utils import create_driver

def test_empty_fields():
    driver = create_driver()

    try:
        driver.get("http://13.61.27.31:5100/login")
        print("Opened login page with empty form")

        # Click login without entering anything
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(2)

        if "login" in driver.current_url:
            print("✅ Empty field validation passed (still on login page)")
        else:
            print("❌ Unexpected behavior on empty login")

    finally:
        driver.quit()
