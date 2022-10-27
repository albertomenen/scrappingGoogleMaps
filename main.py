import gspread
import time 
import re
from selenium import webdriver 
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

class ScrapearGMaps:
  


driver = webdriver.Chrome(executable_path="/Macintosh HD/Usuarios/albertomenendez/Escritorio/Automatiz/googleMaps/chromedriver 2")
time.sleep(3)
driver.quit()
