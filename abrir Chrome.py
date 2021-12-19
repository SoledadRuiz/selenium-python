from selenium import webdriver 
driver= webdriver.Chrome() #creo una variable para Chrome       
driver.get("http://www.youtube.com") #uso la variable driver para abrir (get) tal URL
driver.close() #cerrar servicio para no encimar paginas,siempre parentesis