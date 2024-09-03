from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #Libreria para usar Keys.TAB o Keys ENTER,etc...

driver=webdriver.Firefox()
driver.get("https://fines.educacion.espinlabs.com.ar/administracion/ingresar")

time.sleep(2)
user=driver.find_element(By.XPATH,"//input[contains(@id,'username')]")
user.send_keys("admin@admin.com")
user.send_keys(Keys.TAB +"admin" + Keys.ENTER) 
time.sleep(6)

seguridad=driver.find_element(By.XPATH,"//a[@href='#seguridad'][contains(.,'Seguridad')]")
print(seguridad)

driver.close() #cerrar la pagina

