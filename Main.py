from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
#Navigate to URL
driver.get("https://www.airasia.com/en/gb")

#wait til page is displayed
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,"origin"))
)


#Initialize attributes
tripType = driver.find_element(By.ID,"home_triptype")
origin = driver.find_element(By.ID,"origin")
destination = driver.find_element(By.ID,"destination")
depart_date = driver.find_element(By.ID,"departclick-handle")
return_date = driver.find_element(By.ID,"returnclick-handle")



#Select trip type







#Input origin 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(origin))  # Ensure the element is clickable
origin.click()
origin.send_keys("Kuala Lumpur")
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'suggestions')]")))  # Wait for suggestions to appear
origin.send_keys(Keys.ENTER)

#Input destination
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(destination))
origin.click()
origin.send_keys("Changi Airport")
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'suggestions')]")))  # Wait for suggestions to appear
origin.send_keys(Keys.ENTER)




driver.quit()