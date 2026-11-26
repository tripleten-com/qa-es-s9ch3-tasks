import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Abre la URL especificada en el navegador
driver.get("SERVER URL")

# Pausa la ejecución durante 2 segundos para que la página cargue por completo
time.sleep(2)

# Busca la imagen del logotipo de Urban Routes
logo_image = driver.find_element(By.CSS_SELECTOR, ".logo-image")

# Verifica que la imagen del logotipo de Urban Routes tenga el valor esperado en su atributo alt: "Urban".

# Cierra el navegador y finaliza la sesión de WebDriver
driver.quit()





