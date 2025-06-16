from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import tempfile

opts = Options()
opts.add_argument("--headless=new")  # Use the new headless mode
opts.add_argument("--disable-gpu")
opts.add_argument("--no-sandbox")
opts.add_argument("--window-size=1920,1080")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # Unique temp user data dir

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)

try:
    driver.get("http://13.61.27.31:5100/")
    print("Opened home page")

    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]").click()
        print("Clicked Add to Cart")
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
        print("Opened cart")

        product = driver.find_element(By.CLASS_NAME, "cart-item")
        print("❌ Test Failed: Product added to cart despite missing backend")
    except NoSuchElementException:
        print("✅ Test Passed: Cart action failed as expected")

finally:
    driver.quit()
