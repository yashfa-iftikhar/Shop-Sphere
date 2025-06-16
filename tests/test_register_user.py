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
    driver.get("http://16.171.162.11:5100/register")
    print("Opened register page")

    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")

    driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]").click()
    print("Clicked register")

    time.sleep(3)

    # Expecting registration to fail (e.g. no redirect, no dashboard, no login)
    try:
        driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
        print("❌ Test Failed: User registered even though DB is not connected")
    except NoSuchElementException:
        print("✅ Test Passed: Registration failed as expected (no DB connection)")

finally:
    driver.quit()
