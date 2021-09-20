from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path=r"C:/chromedriver.exe")

MAIN_URL = "https://github.com/LuisLegreaux39/Automation-Clases"
driver.get(MAIN_URL)

PAGINAS = [
    "Code",
    "Issues",
    "Pull requests",
    "Actions",
    "Projects",
    "Wiki",
    "Security",
    "Insights",
    "Settings",
]

for pagina in PAGINAS:
    opcion_de_barra_de_busqueda_git = driver.find_element_by_xpath(
        "//*[@data-content='"+str(pagina)+"']")
    opcion_de_barra_de_busqueda_git.click()
    print("Haciendo click en ==>" + str(pagina))
    time.sleep(5)

time.sleep(10)
driver.close()
