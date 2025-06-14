from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1920,1080")
opts.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)

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
