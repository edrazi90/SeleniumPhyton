from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException, WebDriverException
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)



    
#Navigate to URL
driver.get("https://www.airasia.com/en/gb")
driver.maximize_window()

#wait til page is displayed
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,"origin"))
)


#Initialize attributes
tripType = driver.find_element(By.ID,"home_triptype")
paxSection = driver.find_element(By.ID,"airasia-dropdown-options-title")
origin = driver.find_element(By.ID,"origin")
destination = driver.find_element(By.ID,"destination")
depart_date = driver.find_element(By.ID,"departclick-handle")
return_date = driver.find_element(By.ID,"returnclick-handle")



#Select trip type
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tripType))
tripType.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"home_oneway")))
oneWay = driver.find_element(By.ID,"home_oneway")#declare trip type with ID here
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"home_oneway")))
oneWay.click()
WebDriverWait(driver,5)

#Set pax and travel class
paxSection.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"home_premium_economy")))
premiumEcon = driver.find_element(By.ID,"home_premium_economy")#Initialize Travelclass
premiumEcon.click()



#clear origin & desination  textbox
origin.sendKeys(Keys.CONTROL + "a")
origin.sendKeys(Keys.DELETE)

destination.sendKeys(Keys.CONTROL + "a")
destination.sendKeys(Keys.DELETE)


#Input origin 
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(origin))  # Ensure the element is clickable
origin.click()
origin.send_keys("Kuala Lumpur")
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'suggestions')]")))  # Wait for suggestions to appear
origin.send_keys(Keys.ENTER)

#Input destination
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(destination))
origin.click()
origin.send_keys("Changi Airport")
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'suggestions')]")))  # Wait for suggestions to appear
origin.send_keys(Keys.ENTER)

#Input depart date
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(depart_date))
depart_date.send_keys("1/12/2024")


