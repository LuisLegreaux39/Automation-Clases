# Email: llegreaux@gmail.com
# Author:Luis Legreaux

# Importando la herramienta del webdriver de la libreria selenium
# @ https://pypi.org/project/selenium/
import time
from selenium import webdriver

# Comentario es una linea de codigo que no es ejecutable
# Comenatio son importantes
# Golden path

# Funciones de ayuda


def wait(tiempo):
    # Esta funcion espera una cantidad de segundos [tiempo] deseada
    time.sleep(tiempo)


# Configuraciones
urlPrincipal = str("https://www.google.com/")
rutaDelDriver = str(
    r"C:/Users/Luis Ricardo/Desktop/Programacion/Python_Automation/WebDriver/chromedriver.exe")

# Declaron driver de control principal
driver = webdriver.Chrome(executable_path=rutaDelDriver)
# Entrando a la url principal
driver.get(urlPrincipal)
driver.maximize_window()
wait(10)
# Cerrando driver
driver.close()
