# test_signup_page_load.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://13.61.27.31:5100/login")
    print("Opened login page")

    # Attempt to click on "Register" link/button (update text if needed)
    try:
        driver.find_element(By.LINK_TEXT, "register").click()
        time.sleep(2)
        if "signup" in driver.current_url:
            print("✅ Register page loaded successfully")
        else:
            print("❌ Register link clicked but not redirected correctly")
    except:
        print("❌ Register link not found on login page")

finally:
    driver.quit()
