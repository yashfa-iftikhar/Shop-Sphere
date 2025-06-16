from selenium.webdriver.common.by import By
import time
from utils import create_driver

def test_empty_fields():
    driver = create_driver()

    try:
        driver.get("http://13.61.27.31:5100/login")
        print("Opened login page")

        # Click login without entering any input
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()
        print("Clicked Login with empty fields")

        time.sleep(2)

        current_url = driver.current_url
        if "login" in current_url:
            print("✅ Test Passed: Still on login page due to empty fields")
        else:
            print("❌ Test Failed: Redirected away despite empty fields")

    finally:
        driver.quit()
