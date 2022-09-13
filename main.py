import time 
from selenium import webdriver 


driver = webdriver.Chrome(executable_path="/Macintosh HD/Usuarios/albertomenendez/Escritorio/Automatiz/googleMaps/chromedriver 2")
time.sleep(5)
driver.quit()