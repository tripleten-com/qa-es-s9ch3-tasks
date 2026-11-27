import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa una nueva instancia de Chrome WebDriver
driver = webdriver.Chrome()

# Abre la URL especificada en el navegador
driver.get("SERVER URL")

# Pausa la ejecución durante 5 segundos para que la página cargue por completo
time.sleep(5)

from_field = driver.find_element(By.ID, "from")
time.sleep(5)

from_field.send_keys("East 2nd Street, 601")

time.sleep(5)

# Encuentra el botón de borrado del campo Desde y haz clic en él. Hazlo en una sola instrucción.

# Lee el valor actualizado del campo y comprueba que esté vacío


# Cierra el navegador y finaliza la sesión de WebDriver
driver.quit()