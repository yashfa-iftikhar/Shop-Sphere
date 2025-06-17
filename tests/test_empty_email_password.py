from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)

driver = create_driver()

try:
    driver.get("http://13.61.27.31:5100/login")
    print("Opened login page")

    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(2)

    if "login" in driver.current_url:
        print("✅ Empty field validation passed (still on login page)")
    else:
        print("❌ Unexpected behavior on empty login")

finally:
    driver.quit()
