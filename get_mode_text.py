from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expected_mode = "Flash"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("SERVER URL")

wait = WebDriverWait(driver, 10)

from_field = wait.until(
    EC.visibility_of_element_located((By.ID, "from"))
)
to_field = wait.until(
    EC.visibility_of_element_located((By.ID, "to"))
)

from_field.send_keys("East 2nd Street, 601")
to_field.send_keys("1300 1st St")

wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "modes-container")
    )
)

# Localiza el modo seleccionado
...

# Lee su texto visible
...

assert mode_text == expected_mode
print("Modo seleccionado:", mode_text)

driver.quit()