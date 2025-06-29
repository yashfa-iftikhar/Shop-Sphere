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
    driver.get("http://16.171.162.11:5100/")
    print("Opened home page")

    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]").click()
        print("Clicked Add to Cart")
        time.sleep(2)

        # Check if cart updated or item added
        driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
        print("Opened cart")

        # Check if any product appears
        product = driver.find_element(By.CLASS_NAME, "cart-item")
        print("❌ Test Failed: Product added to cart despite missing backend")
    except NoSuchElementException:
        print("✅ Test Passed: Cart action failed as expected")

finally:
    driver.quit()
