from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path=r"./chromedriver.exe")
MAIN_URL = "https://react-hook-form.com/faqs/"
driver.get(MAIN_URL)
time.sleep(10)
print("Accessing to a page")
driver.close()
