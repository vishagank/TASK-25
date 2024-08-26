from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# Open the IMDb Advanced Name Search URL
driver.get('https://www.imdb.com/search/name/')


wait = WebDriverWait(driver, 10)

driver.maximize_window()

name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
name_input.send_keys("Vishal")

driver.quit()
