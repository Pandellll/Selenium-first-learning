from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# setup chromedriver
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# buka halaman login
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# cari dan isi username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("student")

# cari dan isi password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Password123")

# klik tombol login
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# tunggu beberapa detik untuk melihat hasil
time.sleep(3)

# verifikasi hasil login (cek apakah ada teks sukses)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    success_massage = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME,"h1"))
    )
    if success_massage.text == "Logged in Successfully":
        print("login success")
    else:
        print("login failed")
except:
    print("login failed - element not found")

# tutup browser
driver.quit()