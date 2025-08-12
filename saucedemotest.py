from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#chrome option
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-save-password-")

# path
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

#wait
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user-name"))
)

#fill username & password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

#login
driver.find_element(By.ID, "login-button").click()

#add to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

#cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

#checkout
driver.find_element(By.ID, "checkout").click()

#form checkout
driver.find_element(By.ID, "first-name").send_keys("PanPan")
driver.find_element(By.ID, "last-name").send_keys("Pandel")
driver.find_element(By.ID, "postal-code").send_keys("12345")

#continue
driver.find_element(By.ID, "continue").click()

#finish
driver.find_element(By.ID, "finish").click()

#back to home
driver.find_element(By.ID, "back-to-products").click()

time.sleep(3)
driver.quit()
print("berhasil")