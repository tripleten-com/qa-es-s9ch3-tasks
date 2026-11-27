import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("SERVER URL")

wait = WebDriverWait(driver, 10)

# Esperar a que los campos de dirección sean visibles
from_field = wait.until(
    EC.visibility_of_element_located((By.ID, "from"))
)
to_field = wait.until(
    EC.visibility_of_element_located((By.ID, "to"))
)

from_field.send_keys("East 2nd Street, 601")
to_field.send_keys("1300 1st St")

# Esperar a que el botón para pedir un taxi esté disponible para hacer clic
call_taxi_button = (By.XPATH, '//button[contains(text(), "Pedir un taxi")]')

wait.until(
    EC.element_to_be_clickable(call_taxi_button)
).click()

# Esperar a que el campo de comentarios sea visible
comment_field = wait.until(
    EC.visibility_of_element_located((By.ID, "comment"))
)

# Ingresa el mensaje aquí


# Comprobación del mensaje
assert comment_field.get_property("value") == "Mensaje de prueba"
print("Mensaje ingresado")

# Borra el mensaje aquí


# Finaliza la sesión
driver.quit()