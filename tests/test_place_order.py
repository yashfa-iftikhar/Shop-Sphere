from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from utils import create_driver

def test_checkout_logic_missing():
    driver = create_driver()

    try:
        driver.get("http://13.61.27.31:5100/cart")
        print("Opened cart page")

        try:
            driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]").click()
            print("Clicked checkout")

            time.sleep(3)

            # Verify if any order confirmation is shown
            driver.find_element(By.XPATH, "//h2[contains(text(), 'Order Confirmed')]")
            print("❌ Test Failed: Order placed even though checkout logic is missing")
        except NoSuchElementException:
            print("✅ Test Passed: Order failed as expected (checkout logic missing)")

    finally:
        driver.quit()
