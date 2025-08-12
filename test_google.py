from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ganti sesuai lokasi chromedriver
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# buka halaman google
driver.get("https://www.google.com")

# tunggu 3 detik
time.sleep(3)

# cari input search
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Belajar Selenium Python")
search_box.submit()

#tunggu 5 detik, lalu tutup
time.sleep(5)
driver.quit()