# Google, Buscar palabra dada

# Autor : Luis Medina
# Email: luismedina@gmail.com

# Librerias a utilizar
# Ref: @https://www.selenium.dev/
# Ref: @https://python-para-impacientes.blogspot.com/2017/03/el-modulo-time.html#:~:text=El%20m%C3%B3dulo%20time%20de%20la,con%20fechas%20y%2Fo%20horas.&text=y%20como%20un%20objeto%20struct_time,)%20con%20nueve%20valores%20enteros).

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Helps/Utiles/Funciones


def esperar(tiempo):
    print("Esperando "+str(tiempo)+" Segundos")
    time.sleep(tiempo)


# Configuraciones
ruta_driver = str(
    r"C:/Users/Luis Ricardo/Desktop/Programacion/Python_Automation/WebDriver/chromedriver.exe")
URL = str("https://www.google.com/")
# Configuraciones xpath
xpath_barra_busqueda_google = str("//*[@class='gLFyf gsfi']")

# Pidiendo palabra a buscar
palabra_buscar = str(input("Introdusca una palabra para buscar "))
esperar(5)
# iniciando web driver

driver = webdriver.Chrome(executable_path=ruta_driver)
# Abriendo pagina
print("Accesando a ==> " + URL)
driver.get(URL)
esperar(100)
# Buscando barra de busqueda en la pantalla
barra_busqueda_google = driver.find_element_by_xpath(
    xpath_barra_busqueda_google)

# Escribiendo palabra a buscar
barra_busqueda_google.send_keys(palabra_buscar)
esperar(1)
barra_busqueda_google.send_keys(Keys.ENTER)
esperar(5)
# Cerrando driver
driver.close()


# coleccion de test cases
# Login.py ==>test case

# buscar amigo.py  ==>test case
# Agregar amigo.py  ==>test case

# Flujo buscar amigo
# flujo buscar amigo.py {
# Login.py ==>test case
# buscar amigo.py  ==>test case
# }
