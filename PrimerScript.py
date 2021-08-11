import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def wait(time_to_wait):
    print("Esperando ==> " + str(time_to_wait) + " Milisegundos")
    time.sleep(int(time_to_wait))


def clickOnElement(xpath, driver):
    wait_web_driver = WebDriverWait(driver, 5)
    help_element = wait_web_driver.until(
        expected_conditions.visibility_of_element_located((By.XPATH, str(xpath))))
    print("Cicking ==> " + str(xpath))
    help_element.click()


# Iniciacion de web driver r =route
driver = webdriver.Chrome(
    executable_path=r"C:/Users/Luis Ricardo/Desktop/Programacion/Python_Automation/WebDriver/chromedriver.exe")
# URL
URL = str("https://pypi.org/")
print("Accesando a la pagina ==> " + str(URL))

driver.get(URL)

wait(2)


# xpath_help = str("//*[@class='horizontal-menu__link'][text()='Help']")

# clickOnElement(xpath_help, driver)

# wait(2)

# xpath_login = str("//*[@class='horizontal-menu__link'][text()='Log in']")

# clickOnElement(xpath_login, driver)

xpath_input = "//*[@id='search']"

search_input = driver.find_element_by_xpath(str(xpath_input))

print("Buscando data")

search_input.send_keys("Selenium")

xpath_lupa_boton = "//*[@class='search-form__button']"

boton_lupa = driver.find_element_by_xpath(str(xpath_lupa_boton))

boton_lupa.click()

wait(10)

print("Cerrando Driver")

driver.close()


# WebElement / WebObject
