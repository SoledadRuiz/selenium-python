from selenium import webdriver 
import time #para importar libreria
from selenium.webdriver.common.by import By #para importar la libreria By

driver=webdriver.Firefox()
driver.get("https://fines.educacion.espinlabs.com.ar/administracion/ingresar")

time.sleep(2) #para poner un tiempo de espera, por ejemplo 2 segundos, por eso ()

#user=driver.find_element(By.XPATH,"//input[contains(@id,'username')]")
user=driver.find_element(By.ID,"username")# Uso del selector (ID), arriba ejemplo con XPATH
user.send_keys("admin@admin.com")
time.sleep(2)
contrasena=driver.find_element(By.XPATH,"//input[contains(@id,'password')]") #importado de la libreria By> XPATH
contrasena.send_keys("admin")
time.sleep(2)

#driver.execute_script("window.scrollto(0,300)") > PCOMANDO PARA SCROLLEAR

driver.find_element(By.XPATH,"//button[contains(@id,'btnSubmit')]").click() #click boton
time.sleep(2)



